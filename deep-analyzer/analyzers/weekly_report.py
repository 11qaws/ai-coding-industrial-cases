import sys
import os
import json
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import WEEKLY_SYSTEM_PROMPT, WEEKLY_USER_PROMPT, COMPANY_CONTEXT


def generate_weekly_report(llm, all_articles_text: str, date_str: str) -> dict:
    prompt = WEEKLY_USER_PROMPT.format(
        company_context=COMPANY_CONTEXT,
        date=date_str,
        all_articles_text=all_articles_text,
    )
    result = llm.analyze(WEEKLY_SYSTEM_PROMPT, prompt)
    cleaned = result.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1] if "\n" in cleaned else cleaned[3:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        cleaned = cleaned.strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {"raw": cleaned, "key_findings": [], "week": date_str}
