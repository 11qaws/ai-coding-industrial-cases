import sys
import os
import json
import traceback
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import (
    SEARCH_QUERIES,
    ANALYSIS_SYSTEM_PROMPT,
    ANALYSIS_USER_PROMPT,
    LLM_PROVIDER,
    OUTPUT_DIR,
GITHUB_REPO_URL,
    GITHUB_REPO_DIR,
    OPENCODE_SERVER_URL,
)
from collectors.web_search import search_all
from collectors.arxiv_search import search_arxiv
from collectors.scraper import fetch_page
from reporters.markdown_reporter import generate_daily_report

if LLM_PROVIDER == "opencode":
    from llm.opencode import OpencodeLLM
    llm = OpencodeLLM(server_url=OPENCODE_SERVER_URL)
elif LLM_PROVIDER == "openai":
    from llm.openai import OpenAILLM
    llm = OpenAILLM()
elif LLM_PROVIDER == "anthropic":
    from llm.anthropic import AnthropicLLM
    llm = AnthropicLLM()
else:
    raise ValueError(f"Unknown LLM_PROVIDER: {LLM_PROVIDER}")


def main():
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"[{today}] Starting data collection...")

    print("  [1/4] Searching web...")
    web_results = search_all(SEARCH_QUERIES, max_per_query=8)
    print(f"  -> {len(web_results)} web results")

    print("  [2/4] Searching ArXiv...")
    arxiv_results = search_arxiv(SEARCH_QUERIES, max_results=4)
    print(f"  -> {len(arxiv_results)} arxiv results")

    all_results = web_results + arxiv_results
    if not all_results:
        print("  [WARN] No results found. Exiting.")
        return

    print(f"  [3/4] Analyzing {len(all_results)} articles...")
    analyses = []
    for i, item in enumerate(all_results):
        print(f"    [{i+1}/{len(all_results)}] {item['title'][:60]}...")
        content = fetch_page(item["url"])
        if not content:
            continue
        user_prompt = ANALYSIS_USER_PROMPT.format(
            title=item["title"],
            url=item["url"],
            content=content,
        )
        try:
            result = llm.analyze(ANALYSIS_SYSTEM_PROMPT, user_prompt)
            analysis = _parse_result(result)
            analyses.append({
                "title": item["title"],
                "url": item["url"],
                "source": item["source"],
                "analysis": analysis,
            })
        except Exception as e:
            print(f"    [ERROR] Analysis failed: {e}")
            traceback.print_exc()

    print(f"  [4/4] Generating report...")
    daily_path = os.path.join(OUTPUT_DIR, f"ai-coding-{today}.md")
    generate_daily_report(analyses, daily_path)

    print("  Publishing to GitHub...")
    try:
        from git_publisher import GitPublisher
        publisher = GitPublisher(GITHUB_REPO_SSH, GITHUB_REPO_DIR)
        publisher.publish(OUTPUT_DIR, "daily", f"daily: {today} - {len(analyses)} articles")
    except Exception as e:
        print(f"  [ERROR] GitHub publish failed: {e}")
        traceback.print_exc()

    print(f"[{today}] Done. {len(analyses)} articles collected and analyzed.")


def _parse_result(result: str) -> dict:
    cleaned = result.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1] if "\n" in cleaned else cleaned[3:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        cleaned = cleaned.strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {"raw": cleaned, "key_points": [cleaned]}


if __name__ == "__main__":
    main()
