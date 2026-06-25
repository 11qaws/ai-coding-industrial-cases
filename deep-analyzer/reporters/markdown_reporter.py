import json


def save_pattern_report(data: dict, output_path: str):
    lines = []
    lines.append("# 패턴 및 인사이트 분석 (삼성 파운드리)")
    lines.append(f"## {data.get('date', 'N/A')}")
    lines.append(f"**분석 대상:** {data.get('total_articles_analyzed', 0)}개 기사")
    lines.append("")

    themes = data.get("recurring_themes", [])
    if themes:
        lines.append("## 반복되는 테마")
        for t in themes:
            cat = t.get("category", "")
            icon = {"production": "🏭", "operations": "⚙️", "both": "🔗"}.get(cat, "📌")
            lines.append(f"### {icon} {t.get('theme', 'N/A')} (빈도: {t.get('frequency', 0)})")
            lines.append(f"- **분류:** {cat}")
            lines.append(t.get("description", ""))
            for ex in t.get("examples", []):
                lines.append(f"  - {ex}")
            lines.append("")

    pt = data.get("production_tech_insights", [])
    if pt:
        lines.append("## 생산 기술 인사이트")
        for ins in pt:
            lines.append(f"### {ins.get('insight', 'N/A')}")
            lines.append(f"- **근거:** {ins.get('evidence', '')}")
            lines.append(f"- **적용 공정:** {ins.get('applicable_process', '')}")
            lines.append(f"- **수율 영향:** {ins.get('yield_impact', '')}")
            lines.append("")

    ot = data.get("operations_tech_insights", [])
    if ot:
        lines.append("## 운영 기술 인사이트")
        for ins in ot:
            lines.append(f"### {ins.get('insight', 'N/A')}")
            lines.append(f"- **근거:** {ins.get('evidence', '')}")
            lines.append(f"- **개선 프로세스:** {ins.get('process_improvement', '')}")
            lines.append(f"- **자동화 수준:** {ins.get('automation_level', '')}")
            lines.append("")

    trends = data.get("emerging_trends", [])
    if trends:
        lines.append("## 떠오르는 트렌드")
        for tr in trends:
            sig = tr.get("signal_strength", "medium")
            icon = {"strong": "🔴", "medium": "🟡", "weak": "🟢"}.get(sig, "⚪")
            lines.append(f"- {icon} **{tr.get('trend', 'N/A')}** (신호: {sig})")
            lines.append(f"  {tr.get('details', '')}")
            rel = tr.get("relevance_to_us", "")
            if rel:
                lines.append(f"  **우리 관련성:** {rel}")
            lines.append("")

    gaps = data.get("gaps_and_opportunities", [])
    if gaps:
        lines.append("## 정보 격차 및 기회")
        for g in gaps:
            lines.append(f"- **격차:** {g.get('gap', '')}")
            lines.append(f"  **기회:** {g.get('opportunity', '')}")
            lines.append(f"  **내부 관련성:** {g.get('internal_relevance', '')}")
            lines.append("")

    afs = data.get("adoption_feasibility_summary", {})
    if afs:
        lines.append("## 도입 가능성 요약")
        for qw in afs.get("quickest_wins", []):
            lines.append(f"- ⚡ **Quick Win:** {qw}")
        for hp in afs.get("highest_priority", []):
            lines.append(f"- 🎯 **최우선:** {hp}")
        for cr in afs.get("common_risks", []):
            lines.append(f"- ⚠️ **공통 리스크:** {cr}")
        lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [OK] Pattern report saved: {output_path}")


def save_technology_report(data: dict, output_path: str):
    lines = []
    lines.append("# 기술 심층 분석 (삼성 파운드리)")
    lines.append(f"## {data.get('date', 'N/A')}")
    lines.append("")

    for tech in data.get("technologies", []):
        lines.append(f"## {tech.get('technology', 'N/A')}")
        cat = tech.get("category", "")
        lines.append(f"- **카테고리:** {cat}")
        lines.append(f"- **사례 수:** {tech.get('case_count', 0)}")
        lines.append("")
        lines.append(f"### 개요")
        lines.append(tech.get("overview", ""))
        lines.append("")

        pa = tech.get("production_applications", [])
        if pa:
            lines.append(f"### 생산 기술 적용")
            for p in pa:
                lines.append(f"- **공정:** {p.get('process', '')}")
                lines.append(f"  적용: {p.get('application', '')}")
                lines.append(f"  효과: {p.get('expected_impact', '')}")
                lines.append("")

        oa = tech.get("operations_applications", [])
        if oa:
            lines.append(f"### 운영 기술 적용")
            for o in oa:
                lines.append(f"- **영역:** {o.get('area', '')}")
                lines.append(f"  적용: {o.get('application', '')}")
                lines.append(f"  프로세스 변경: {o.get('process_change', '')}")
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

        idep = tech.get("internal_deployment", {})
        if idep:
            lines.append("### 내부 배포 검토")
            lines.append(f"- **내부망 가능성:** {idep.get('air_gap_feasibility', '')}")
            lines.append(f"- **데이터 요구사항:** {idep.get('data_requirements', '')}")
            lines.append(f"- **통합 복잡도:** {idep.get('integration_complexity', '')}")
            lines.append(f"- **예상 기간:** {idep.get('estimated_timeline_months', '')}개월")
            lines.append("")

        lines.append(f"### 제안")
        for r in tech.get("recommendations", []):
            lines.append(f"- {r}")
        lines.append("---")
        lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [OK] Technology deepdive saved: {output_path}")


def save_weekly_report(data: dict, output_path: str):
    lines = []
    lines.append("# 주간 종합 리포트 (삼성 파운드리)")
    lines.append(f"## {data.get('week', 'N/A')} ({data.get('period', 'N/A')})")
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
            cat = f.get("category", "")
            icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(imp, "⚪")
            cat_icon = {"production": "🏭", "operations": "⚙️"}.get(cat, "📌")
            lines.append(f"- {icon} {cat_icon} **{f.get('finding', '')}**")
            lines.append(f"  {f.get('detail', '')}")
            sf = f.get("for_samsung", "")
            if sf:
                lines.append(f"  **→ {sf}**")
            lines.append("")

    landscape = data.get("technology_landscape", {})
    if landscape:
        lines.append("## 기술 현황")
        for sector in ["production_tech", "operations_tech"]:
            label = {"production_tech": "생산 기술", "operations_tech": "운영 기술"}.get(sector, sector)
            data_sector = landscape.get(sector, {})
            if data_sector:
                lines.append(f"### {label}")
                for ma in data_sector.get("most_adopted", []):
                    lines.append(f"- ✅ **널리 도입:** {ma}")
                for em in data_sector.get("emerging", []):
                    lines.append(f"- 🌱 **떠오름:** {em}")
                for sr in data_sector.get("samsung_relevant", []):
                    lines.append(f"- ⭐ **삼성 관련:** {sr}")
                lines.append("")

    metrics = data.get("metrics_compilation", [])
    if metrics:
        lines.append("## 지표 종합")
        for m in metrics:
            lines.append(f"### {m.get('category', 'N/A')} (출처: {m.get('source_count', 0)}개)")
            for v in m.get("values", []):
                lines.append(f"- {v}")
            lines.append(f"  **범위:** {m.get('range', 'N/A')}")
            lines.append("")

    roadmap = data.get("adoption_roadmap", {})
    if roadmap:
        lines.append("## 도입 로드맵")
        for period, key in [("즉시 (0-3개월)", "immediate_0_3_months"),
                            ("단기 (3-6개월)", "short_3_6_months"),
                            ("중기 (6-12개월)", "medium_6_12_months")]:
            actions = roadmap.get(key, [])
            if actions:
                lines.append(f"### {period}")
                for a in actions:
                    lines.append(f"- **{a.get('action', '')}**")
                    lines.append(f"  {a.get('rationale', '')}")
                    lines.append("")

    recs = data.get("recommendations", [])
    if recs:
        lines.append("## 제안")
        for r in recs:
            prio = r.get("priority", "medium")
            icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(prio, "⚪")
            lines.append(f"- {icon} **[{prio.upper()}] {r.get('recommendation', '')}**")
            lines.append(f"  {r.get('rationale', '')}")
            roi = r.get("expected_roi", "")
            if roi:
                lines.append(f"  **ROI:** {roi}")
            lines.append("")

    lines.append("---")
    lines.append("*이 리포트는 AI 기반 분석을 통해 생성되었습니다. 정확성 검증이 필요할 수 있습니다.*")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [OK] Weekly report saved: {output_path}")
