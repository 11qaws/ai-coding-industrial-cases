from .base import LLM


class OpenAILLM(LLM):
    def __init__(self, api_key: str = "", model: str = "gpt-4o-mini"):
        self.api_key = api_key
        self.model = model

    def analyze(self, system_prompt: str, user_content: str) -> str:
        raise NotImplementedError("OpenAI provider not yet configured. Set OPENAI_API_KEY.")
