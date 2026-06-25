from .base import LLM


class AnthropicLLM(LLM):
    def __init__(self, api_key: str = "", model: str = "claude-sonnet-4-20250514"):
        self.api_key = api_key
        self.model = model

    def analyze(self, system_prompt: str, user_content: str) -> str:
        raise NotImplementedError("Anthropic provider not yet configured. Set ANTHROPIC_API_KEY.")
