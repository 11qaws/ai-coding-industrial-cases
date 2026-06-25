import json
from datetime import datetime, timezone
from typing import List, Dict


def generate_daily_report(analyses: List[Dict], output_path: str):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = []
    lines.append("# 삼성 파운드리 AI 도입 연구 - 일일 리포트")
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

        # Key Points
        kps = a.get("key_points", [])
        if kps:
            lines.append("#### Key Points")
            for j, kp in enumerate(kps, 1):
                lines.append(f"{j}. {kp}")
            lines.append("")

        # Notable Aspects
        nas = a.get("notable_aspects", [])
        if nas:
            lines.append("#### Notable Aspects")
            for j, na in enumerate(nas, 1):
                lines.append(f"{j}. {na}")
            lines.append("")

        # Core Highlights
        ch = a.get("core_highlights", "")
        if ch:
            lines.append("#### Core Highlights")
            lines.append(f"> **{ch}**")
            lines.append("")

        # For Engineers
        fe = a.get("for_engineers", {})
        if fe:
            lines.append("#### For Engineers")
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

        # Internal Lens
        il = a.get("internal_lens", {})
        if il:
            lines.append("#### Internal Lens (삼성 파운드리 관점)")

            eg = il.get("environment_gap", "")
            if eg:
                lines.append(f"- **환경 차이:** {eg}")

            pt = il.get("production_tech", {})
            if pt:
                lines.append("- **생산 기술 관점:**")
                for k, v in pt.items():
                    if v:
                        lines.append(f"  - {_label(k)}: {v}")

            ot = il.get("operations_tech", {})
            if ot:
                lines.append("- **운영 기술 관점:**")
                for k, v in ot.items():
                    if v:
                        lines.append(f"  - {_label(k)}: {v}")

            ci = il.get("constraint_impact", [])
            if ci:
                lines.append("- **제약사항 영향:**")
                for c in ci:
                    lines.append(f"  - {c}")

            qw = il.get("quick_wins", [])
            if qw:
                lines.append("- **Quick Wins:**")
                for q in qw:
                    lines.append(f"  - {q}")

            ad = il.get("adaptations", [])
            if ad:
                lines.append("- **적용 시 수정사항:**")
                for a2 in ad:
                    lines.append(f"  - {a2}")

            pr = il.get("priority_for_us", "")
            pr_reason = il.get("priority_reason", "")
            if pr:
                lines.append(f"- **우선순위:** {pr} - {pr_reason}")
            lines.append("")

        # Adoption Feasibility
        af = a.get("adoption_feasibility", {})
        if af:
            lines.append("#### 도입 가능성")
            diff = af.get("difficulty", "")
            diff_reason = af.get("difficulty_reason", "")
            if diff:
                lines.append(f"- **난이도:** {diff} - {diff_reason}")
            for k in ["required_resources", "prerequisites"]:
                vals = af.get(k, [])
                if vals:
                    lines.append(f"- **{_label(k)}:**")
                    for v in vals:
                        lines.append(f"  - {v}")
            risks = af.get("risks", [])
            if risks:
                lines.append("- **리스크:**")
                for r in risks:
                    risk_text = r.get("risk", "")
                    mitigation = r.get("mitigation", "")
                    if mitigation:
                        lines.append(f"  - {risk_text} → {mitigation}")
                    else:
                        lines.append(f"  - {risk_text}")
            roi = af.get("roi_estimate", "")
            if roi:
                lines.append(f"- **ROI 추정:** {roi}")
            checklist = af.get("checklist", [])
            if checklist:
                lines.append("- **의사결정 체크리스트:**")
                for c in checklist:
                    lines.append(f"  - [ ] {c}")
            lines.append("")

        # Milestones
        ms = a.get("milestones", {})
        if ms:
            lines.append("#### 실행 마일스톤")
            total = ms.get("total_duration_months", "")
            if total:
                lines.append(f"**전체 예상 기간:** {total}개월")
            lines.append("")
            lines.append("| 단계 | 기간(월) | 주요 활동 | 산출물 | Decision Gate |")
            lines.append("|------|----------|----------|--------|---------------|")
            for phase in ms.get("phases", []):
                pname = phase.get("phase", "")
                dur = phase.get("duration", "")
                if dur is None:
                    dur = "∞"
                acts = ", ".join(phase.get("activities", []))[:40]
                dels = ", ".join(phase.get("deliverables", []))[:40]
                gate = phase.get("gate", "")
                lines.append(f"| {pname} | {dur} | {acts} | {dels} | {gate} |")
            lines.append("")

        # Tags
        tags = a.get("tags", [])
        if tags:
            lines.append(f"**태그:** `{'`, `'.join(tags)}`")
            lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [OK] Report saved: {output_path} ({len(analyses)} articles)")


def _label(key: str) -> str:
    labels = {
        "environment_gap": "환경 차이",
        "applicable_process": "적용 가능 공정",
        "yield_impact": "수율 영향",
        "equipment_compatibility": "장비 호환성",
        "applicable_area": "적용 영역",
        "process_improvement": "프로세스 개선",
        "interface_impact": "인터페이스 영향",
        "automation_level": "자동화 수준",
        "required_resources": "필요 자원",
        "prerequisites": "선행 조건",
        "priority_for_us": "우선순위",
        "priority_reason": "우선순위 이유",
        "constraint_impact": "제약사항 영향",
        "quick_wins": "Quick Wins",
        "adaptations": "적용 시 수정사항",
    }
    return labels.get(key, key)
