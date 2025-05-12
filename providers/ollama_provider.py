from __future__ import annotations
from openai import AsyncOpenAI
from agents import (
    Model,
    ModelProvider,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)

BASE_URL = "http://localhost:11434/v1"
API_KEY = "ollama-placeholder-key"
MODEL_NAME = "mistral"

#if not BASE_URL or not API_KEY or not MODEL_NAME:
#    raise ValueError(
#        "Please set EXAMPLE_BASE_URL, EXAMPLE_API_KEY, EXAMPLE_MODEL_NAME via env var or code."
#         )

client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)
set_tracing_disabled(disabled=True)

class CustomModelProvider(ModelProvider):
    def get_model(self, model_name: str | None) -> Model:
        return OpenAIChatCompletionsModel(model=model_name or MODEL_NAME, openai_client=client)


