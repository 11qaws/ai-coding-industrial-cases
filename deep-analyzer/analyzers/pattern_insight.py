import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import PATTERN_SYSTEM_PROMPT


def analyze_patterns(llm, all_articles_text: str, date_str: str) -> dict:
    prompt = f"""Today's date: {date_str}

Here are all collected articles and their analyses:

{all_articles_text}

Identify cross-cutting patterns, recurring themes, emerging trends, and gaps across these case studies."""
    result = llm.analyze(PATTERN_SYSTEM_PROMPT, prompt)
    cleaned = result.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1] if "\n" in cleaned else cleaned[3:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        cleaned = cleaned.strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {"raw": cleaned, "recurring_themes": []}
