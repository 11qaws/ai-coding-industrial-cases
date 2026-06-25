import requests
import json

from .base import LLM


class OpencodeLLM(LLM):
    def __init__(self, server_url: str = "http://127.0.0.1:14097"):
        self.server_url = server_url

    def analyze(self, system_prompt: str, user_content: str) -> str:
        ses = requests.post(
            f"{self.server_url}/session",
            json={"title": "deep-analyze"},
        )
        ses.raise_for_status()
        session_id = ses.json()["id"]
        try:
            body = {
                "model": None,
                "noReply": True,
                "parts": [
                    {"type": "text", "text": f"{system_prompt}\n\n{user_content}"}
                ],
            }
            resp = requests.post(
                f"{self.server_url}/session/{session_id}/message",
                json=body,
                timeout=300,
            )
            resp.raise_for_status()
            data = resp.json()
            for part in data.get("parts", []):
                if part.get("type") == "text":
                    return part.get("text", "")
            return json.dumps(data.get("parts", []))
        finally:
            try:
                requests.delete(f"{self.server_url}/session/{session_id}")
            except Exception:
                pass
