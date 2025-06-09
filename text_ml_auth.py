from starlette.requests import Request
from typing import Dict
import ray
from ray import serve
from ray.serve.handle import DeploymentHandle
from transformers import pipeline
import asyncio

# === In-memory API Key Store ===
API_KEYS = {
    "my-secret-key-1": "key1",
    "my-secret-key-2": "key2"
}

# === Per-API-Key Usage Counter ===
API_USAGE = {k: 0 for k in API_KEYS}


@serve.deployment(
    autoscaling_config={
        "min_replicas": 1,
        "max_replicas": 10,
        "target_num_ongoing_requests_per_replica": 2,
        "upscale_delay_s": 0,
        "downscale_delay_s": 60
    }
)
class Translator:
    def __init__(self):
        self.language = "french"
        self.model = pipeline("translation_en_to_fr", model="t5-small")

    def translate(self, text: str) -> str:
        model_output = self.model(text)
        return model_output[0]["translation_text"]

    def reconfigure(self, config: Dict):
        self.language = config.get("language", "french")
        if self.language.lower() == "french":
            self.model = pipeline("translation_en_to_fr", model="t5-small")
        elif self.language.lower() == "german":
            self.model = pipeline("translation_en_to_de", model="t5-small")
        elif self.language.lower() == "romanian":
            self.model = pipeline("translation_en_to_ro", model="t5-small")


@serve.deployment(
    autoscaling_config={
        "min_replicas": 1,
        "max_replicas": 10,
        "target_num_ongoing_requests_per_replica": 2,
        "upscale_delay_s": 0,
        "downscale_delay_s": 60
    }
)
class Summarizer:
    def __init__(self, translator: DeploymentHandle):
        self.model = pipeline("summarization", model="t5-small")
        self.translator = translator
        self.min_length = 5
        self.max_length = 15

    def summarize(self, text: str) -> str:
        output = self.model(text, min_length=self.min_length, max_length=self.max_length)
        return output[0]["summary_text"]

    async def __call__(self, http_request: Request) -> str:
        # --- API Key Auth ---
        api_key = http_request.headers.get("x-api-key")
        if api_key not in API_KEYS:
            return "Unauthorized: Invalid API Key"

        # --- Usage Tracking ---
        API_USAGE[api_key] += 1
        print(f"API Key {api_key} used {API_USAGE[api_key]} time(s).")

        # --- Inference ---
        data = await http_request.json()
        english_text = data.get("text")
        summary = self.summarize(english_text)
        return await self.translator.translate.remote(summary)

    def reconfigure(self, config: Dict):
        self.min_length = config.get("min_length", 5)
        self.max_length = config.get("max_length", 15)


# Bind the translator and summarizer
appauth = Summarizer.bind(Translator.bind())