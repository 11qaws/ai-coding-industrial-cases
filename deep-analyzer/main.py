import sys
import os
import json
import traceback
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import (
    LLM_PROVIDER,
    OPENCODE_SERVER_URL,
    GITHUB_REPO_URL,
    GITHUB_REPO_DIR,
    INSIGHT_OUTPUT_DIR,
    DEEPDIVE_OUTPUT_DIR,
    WEEKLY_OUTPUT_DIR,
)
from git_publisher import GitPublisher

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
    week_number = datetime.now(timezone.utc).strftime("%Y-W%W")
    is_sunday = datetime.now(timezone.utc).weekday() == 6

    os.makedirs(INSIGHT_OUTPUT_DIR, exist_ok=True)
    os.makedirs(DEEPDIVE_OUTPUT_DIR, exist_ok=True)
    os.makedirs(WEEKLY_OUTPUT_DIR, exist_ok=True)

    print(f"[{today}] Starting deep analysis...")

    publisher = GitPublisher(GITHUB_REPO_URL, GITHUB_REPO_DIR)
    all_text = publisher.read_daily_files()
    if not all_text:
        print("  [WARN] No daily data found in repo. Exiting.")
        return

    print(f"  [1/3] Running pattern/insight analysis...")
    from analyzers.pattern_insight import analyze_patterns
    try:
        pattern_data = analyze_patterns(llm, all_text, today)
        insight_path = os.path.join(INSIGHT_OUTPUT_DIR, f"insights-{today}.md")
        from reporters.markdown_reporter import save_pattern_report
        save_pattern_report(pattern_data, insight_path)
    except Exception as e:
        print(f"  [ERROR] Pattern analysis failed: {e}")
        traceback.print_exc()

    print(f"  [2/3] Running technology deep-dive...")
    from analyzers.technology_deepdive import analyze_technologies
    try:
        tech_data = analyze_technologies(llm, all_text, today)
        deepdive_path = os.path.join(DEEPDIVE_OUTPUT_DIR, f"deepdive-{today}.md")
        from reporters.markdown_reporter import save_technology_report
        save_technology_report(tech_data, deepdive_path)
    except Exception as e:
        print(f"  [ERROR] Technology deepdive failed: {e}")
        traceback.print_exc()

    if is_sunday:
        print(f"  [3/3] Generating weekly report...")
        from analyzers.weekly_report import generate_weekly_report
        try:
            weekly_data = generate_weekly_report(llm, all_text, today)
            weekly_path = os.path.join(WEEKLY_OUTPUT_DIR, f"weekly-{week_number}.md")
            from reporters.markdown_reporter import save_weekly_report
            save_weekly_report(weekly_data, weekly_path)
        except Exception as e:
            print(f"  [ERROR] Weekly report failed: {e}")
            traceback.print_exc()
    else:
        print(f"  [3/3] Skipping weekly report (not Sunday)")

    print(f"  Publishing deep analysis to GitHub...")
    try:
        publisher.publish(INSIGHT_OUTPUT_DIR, "insights",
                          f"insights: {today} - pattern analysis")
        publisher.publish(DEEPDIVE_OUTPUT_DIR, "deepdive",
                          f"deepdive: {today} - technology analysis")
        if is_sunday:
            publisher.publish(WEEKLY_OUTPUT_DIR, "weekly",
                              f"weekly: {week_number} - comprehensive report")
    except Exception as e:
        print(f"  [ERROR] GitHub publish failed: {e}")
        traceback.print_exc()

    print(f"[{today}] Deep analysis complete.")


if __name__ == "__main__":
    main()
