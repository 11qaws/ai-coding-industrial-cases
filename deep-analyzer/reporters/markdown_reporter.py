import json
from typing import List, Dict


def save_pattern_report(data: dict, output_path: str):
    lines = []
    lines.append("# 패턴 및 인사이트 분석")
    lines.append(f"## {data.get('date', 'N/A')}")
    lines.append("")
    lines.append(f"**분석 대상:** {data.get('total_articles_analyzed', 0)}개 기사")
    lines.append("")

    themes = data.get("recurring_themes", [])
    if themes:
        lines.append("## 반복되는 테마")
        for t in themes:
            lines.append(f"### {t.get('theme', 'N/A')} (빈도: {t.get('frequency', 0)})")
            lines.append(t.get("description", ""))
            for ex in t.get("examples", []):
                lines.append(f"- {ex}")
            lines.append("")

    insights = data.get("cross_cutting_insights", [])
    if insights:
        lines.append("## 교차 인사이트")
        for ins in insights:
            lines.append(f"### {ins.get('insight', 'N/A')}")
            lines.append(f"- **근거:** {ins.get('evidence', '')}")
            lines.append(f"- **시사점:** {ins.get('implication', '')}")
            lines.append("")

    trends = data.get("emerging_trends", [])
    if trends:
        lines.append("## 떠오르는 트렌드")
        for tr in trends:
            sig = tr.get("signal_strength", "medium")
            icon = {"strong": "🔴", "medium": "🟡", "weak": "🟢"}.get(sig, "⚪")
            lines.append(f"- {icon} **{tr.get('trend', 'N/A')}** (신호: {sig})")
            lines.append(f"  {tr.get('details', '')}")
            lines.append("")

    gaps = data.get("gaps_and_opportunities", [])
    if gaps:
        lines.append("## 정보 격차 및 기회")
        for g in gaps:
            lines.append(f"- **격차:** {g.get('gap', '')}")
            lines.append(f"  **기회:** {g.get('opportunity', '')}")
            lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [OK] Pattern report saved: {output_path}")


def save_technology_report(data: dict, output_path: str):
    lines = []
    lines.append("# 기술 심층 분석")
    lines.append(f"## {data.get('date', 'N/A')}")
    lines.append("")

    for tech in data.get("technologies", []):
        lines.append(f"## {tech.get('technology', 'N/A')}")
        lines.append(f"- **카테고리:** {tech.get('category', 'N/A')}")
        lines.append(f"- **사례 수:** {tech.get('case_count', 0)}")
        lines.append("")
        lines.append(f"### 개요")
        lines.append(tech.get("overview", ""))
        lines.append("")
        lines.append(f"### 도입 패턴")
        for p in tech.get("adoption_patterns", []):
            lines.append(f"- {p}")
        lines.append("")
        lines.append(f"### 성공 요인")
        for f in tech.get("success_factors", []):
            lines.append(f"- {f}")
        lines.append("")
        lines.append(f"### 도전 과제")
        for c in tech.get("challenges", []):
            lines.append(f"- {c}")
        lines.append("")
        lines.append(f"### 주요 지표")
        for m in tech.get("key_metrics", []):
            lines.append(f"- {m}")
        lines.append("")
        lines.append(f"### 제안")
        for r in tech.get("recommendations", []):
            lines.append(f"- {r}")
        lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [OK] Technology deepdive saved: {output_path}")


def save_weekly_report(data: dict, output_path: str):
    lines = []
    lines.append("# 주간 종합 리포트")
    lines.append(f"## {data.get('week', 'N/A')} ({data.get('period', 'N/A')})")
    lines.append("")
    lines.append(f"**분석 기사 수:** {data.get('total_articles', 0)}")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append(data.get("executive_summary", ""))
    lines.append("")

    findings = data.get("key_findings", [])
    if findings:
        lines.append("## 주요 발견")
        for f in findings:
            imp = f.get("importance", "medium")
            icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(imp, "⚪")
            lines.append(f"- {icon} **{f.get('finding', '')}**")
            lines.append(f"  {f.get('detail', '')}")
            lines.append("")

    landscape = data.get("technology_landscape", {})
    if landscape:
        lines.append("## 기술 현황")
        for ma in landscape.get("most_adopted", []):
            lines.append(f"- ✅ **널리 도입:** {ma}")
        for em in landscape.get("emerging", []):
            lines.append(f"- 🌱 **떠오르는 기술:** {em}")
        for de in landscape.get("declining", []):
            lines.append(f"- 📉 **주춤:** {de}")
        lines.append("")

    metrics = data.get("metrics_compilation", [])
    if metrics:
        lines.append("## 지표 종합")
        for m in metrics:
            lines.append(f"### {m.get('category', 'N/A')}")
            for v in m.get("reported_values", []):
                lines.append(f"- {v}")
            lines.append(f"  범위: {m.get('range', 'N/A')}")
            lines.append("")

    recs = data.get("recommendations", [])
    if recs:
        lines.append("## 제안")
        for r in recs:
            prio = r.get("priority", "medium")
            icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(prio, "⚪")
            lines.append(f"- {icon} **[{prio.upper()}] {r.get('recommendation', '')}**")
            lines.append(f"  {r.get('rationale', '')}")
            lines.append("")

    lines.append("---")
    lines.append("*이 리포트는 AI 기반 분석을 통해 생성되었습니다. 정확성 검증이 필요할 수 있습니다.*")
    lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [OK] Weekly report saved: {output_path}")
