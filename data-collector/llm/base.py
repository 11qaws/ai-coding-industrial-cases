from abc import ABC, abstractmethod

class LLM(ABC):
    @abstractmethod
    def analyze(self, system_prompt: str, user_content: str) -> str:
        pass
