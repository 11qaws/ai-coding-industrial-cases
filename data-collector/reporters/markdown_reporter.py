import json
from datetime import datetime, timezone
from typing import List, Dict


def generate_daily_report(analyses: List[Dict], output_path: str):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = []
    lines.append(f"# Vibe Coding in Manufacturing - 일일 리포트")
    lines.append(f"## {today} | 총 {len(analyses)}개 사례")
    lines.append("")

    for i, item in enumerate(analyses, 1):
        a = item.get("analysis", {})
        if isinstance(a, str):
            try:
                a = json.loads(a)
            except json.JSONDecodeError:
                a = {"key_points": [a], "relevance": "medium"}

        title = a.get("title", item.get("title", "N/A"))
        url = item.get("url", "")
        source_type = item.get("source", "web")
        relevance = a.get("relevance", "medium")

        lines.append("---")
        lines.append(f"### {i}. {title}")
        lines.append(f"**출처:** [{url}]({url}) | **유형:** {source_type} | **관련도:** {relevance}")
        lines.append("")

        kps = a.get("key_points", [])
        if kps:
            lines.append("#### Key Points")
            for j, kp in enumerate(kps, 1):
                lines.append(f"{j}. {kp}")
            lines.append("")

        nas = a.get("notable_aspects", [])
        if nas:
            lines.append("#### Notable Aspects")
            for j, na in enumerate(nas, 1):
                lines.append(f"{j}. {na}")
            lines.append("")

        ch = a.get("core_highlights", "")
        if ch:
            lines.append("#### Core Highlights")
            lines.append(f"> **{ch}**")
            lines.append("")

        fe = a.get("for_engineers", {})
        if fe:
            lines.append("#### For Manufacturing Engineers")
            tasks = fe.get("implementation_tasks", [])
            if tasks:
                lines.append("- **도입 작업:**")
                for t in tasks:
                    lines.append(f"  - {t}")
            benefits = fe.get("benefits", [])
            if benefits:
                lines.append("- **기대 효과:**")
                for b in benefits:
                    lines.append(f"  - {b}")
            metrics = fe.get("metrics", [])
            if metrics:
                lines.append("- **구체적 지표:**")
                for m in metrics:
                    lines.append(f"  - {m}")
            lines.append("")

        tags = a.get("tags", [])
        if tags:
            lines.append(f"**태그:** `{'`, `'.join(tags)}`")
            lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [OK] Report saved: {output_path}")
