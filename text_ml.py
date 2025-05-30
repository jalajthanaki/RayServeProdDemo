from starlette.requests import Request
from typing import Dict

import ray
from ray import serve
from ray.serve.handle import DeploymentHandle

from transformers import pipeline


@serve.deployment(# Start with 2 replicas
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

        translation = model_output[0]["translation_text"]

        return translation

    def reconfigure(self, config: Dict):
        self.language = config.get("language", "french")

        if self.language.lower() == "french":
            self.model = pipeline("translation_en_to_fr", model="t5-small")
        elif self.language.lower() == "german":
            self.model = pipeline("translation_en_to_de", model="t5-small")
        elif self.language.lower() == "romanian":
            self.model = pipeline("translation_en_to_ro", model="t5-small")
        else:
            pass


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
        # Load model
        self.model = pipeline("summarization", model="t5-small")
        self.translator = translator
        self.min_length = 5
        self.max_length = 15

    def summarize(self, text: str) -> str:
        # Run inference
        model_output = self.model(
            text, min_length=self.min_length, max_length=self.max_length
        )

        # Post-process output to return only the summary text
        summary = model_output[0]["summary_text"]

        return summary

    async def __call__(self, http_request: Request) -> str:
        english_text: str = await http_request.json()
        summary = self.summarize(english_text)

        return await self.translator.translate.remote(summary)

    def reconfigure(self, config: Dict):
        self.min_length = config.get("min_length", 5)
        self.max_length = config.get("max_length", 15)


app = Summarizer.bind(Translator.bind())
