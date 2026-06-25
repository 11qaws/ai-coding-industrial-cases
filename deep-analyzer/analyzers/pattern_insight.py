import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import PATTERN_SYSTEM_PROMPT, PATTERN_USER_PROMPT, COMPANY_CONTEXT


def analyze_patterns(llm, all_articles_text: str, date_str: str) -> dict:
    prompt = PATTERN_USER_PROMPT.format(
        company_context=COMPANY_CONTEXT,
        date=date_str,
        all_articles_text=all_articles_text,
    )
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
        return {"raw": cleaned, "recurring_themes": [], "date": date_str}
