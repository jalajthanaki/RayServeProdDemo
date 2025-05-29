from openai import OpenAI

# Initialize client
client = OpenAI(base_url="http://localhost:8000/v1", api_key="fake-key")

# Request structured JSON output
response = client.chat.completions.create(
    model="qwen-1.5b",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that outputs JSON."
        },
        {
            "role": "user",
            "content": "List three colors in JSON format"
        }
    ],
    stream=True,
)

for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
# Example response:
# {
#   "colors": [
#     "red",
#     "blue",
#     "green"
#   ]
# }
