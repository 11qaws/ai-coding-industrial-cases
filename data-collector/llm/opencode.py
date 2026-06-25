import requests
import json
import time
import sys

from .base import LLM


class OpencodeLLM(LLM):
    def __init__(self, server_url: str = "http://127.0.0.1:14097"):
        self.server_url = server_url

    def analyze(self, system_prompt: str, user_content: str) -> str:
        ses = requests.post(
            f"{self.server_url}/session",
            json={"title": "data-analyze"},
        )
        ses.raise_for_status()
        session_id = ses.json()["id"]

        try:
            body = {
                "system": system_prompt,
                "parts": [
                    {"type": "text", "text": user_content}
                ],
            }
            resp = requests.post(
                f"{self.server_url}/session/{session_id}/message",
                json=body,
                timeout=300,
            )
            resp.raise_for_status()
            data = resp.json()
            text_parts = []
            for part in data.get("parts", []):
                if part.get("type") == "text":
                    text_parts.append(part.get("text", ""))
            return "\n".join(text_parts) if text_parts else json.dumps(data.get("parts", []))
        finally:
            try:
                requests.delete(f"{self.server_url}/session/{session_id}")
            except Exception:
                pass
