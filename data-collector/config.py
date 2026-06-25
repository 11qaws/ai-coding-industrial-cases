from datetime import datetime, timezone

LLM_PROVIDER = "opencode"
OPENCODE_SERVER_URL = "http://127.0.0.1:14097"
GITHUB_REPO_URL = "https://github.com/11qaws/ai-coding-industrial-cases.git"
GITHUB_REPO_DIR = "/home/qumin/discord/data-collector/repo"

OUTPUT_DIR = "/home/qumin/discord/data-collector/output/daily"

COMPANY_CONTEXT = """
- 회사: 삼성전자 DS 부문 파운드리사업부
- 사업: 반도체 웨이퍼 가공 (Foundry), 경쟁사 TSMC/Intel Foundry
- 환경: 국가핵심기술 → 내부망(air-gapped) 전용, 엄격한 보안 정책
- 제약: 접근 불가능한 데이터 다수, 여러 DB 혼재 및 DB 간 통합 미흡
- IT: 개발 친화적이지 않은 환경, 제한된 도구/인프라
- 주요 관심사:
  생산 기술: 수율(Yield) 개선, 공정 안정성, 설비 효율(OEE), 품질 불량률 감소
  운영 기술: MES 고도화, 생산 스케줄링, FDC/R2R 자동화, 레시피 관리,
            ADC(자동결함분류), SOP 자동화, 의사결정 자동화, 인터페이스 통합
"""

SEARCH_QUERIES = [
    # Production Tech (생산 기술)
    "AI manufacturing case study productivity improvement percent",
    "LLM manufacturing quality control defect reduction results",
    "machine learning production line optimization efficiency gain",
    "AI predictive maintenance manufacturing cost savings metrics",
    "deep learning industrial automation throughput increase",
    "computer vision manufacturing inspection accuracy rate",
    "generative AI manufacturing digital twin results",
    "semiconductor foundry AI yield improvement case",
    "AI semiconductor process optimization results",
    # Operations Tech (생산 운영 기술)
    "AI production scheduling semiconductor foundry",
    "MES AI integration manufacturing operations",
    "automated decision system wafer fab",
    "AI recipe optimization semiconductor manufacturing",
    "machine learning fault detection classification semiconductor",
    "AI advanced process control run-to-run semiconductor",
    "AI manufacturing execution system automation",
    "automated defect classification ADC semiconductor AI",
    "AI interface automation fab equipment integration",
    # Korean (국내 사례)
    "제조업 AI 도입 생산성 향상 사례 지표",
    "AI 스마트팩토리 불량률 개선 효과",
    "제조 현장 AI 품질관리 도입 성과",
    "AI 제조공정 최적화 비용 절감",
    "반도체 AI 수율 개선 사례",
    "AI 생산 스케줄링 반도체 공장",
    "AI 기반 반도체 FDC R2R 자동화",
    "MES AI 연동 제조 실행 시스템 고도화",
    "반도체 설비 AI 예지보전 사례",
    "AI ADC 자동결함분류 반도체 적용",
]

ANALYSIS_SYSTEM_PROMPT = """You are a technical analyst specializing in AI applications in semiconductor manufacturing (Foundry). Analyze the given article and provide a structured analysis.

ABSOLUTE RULES:
1. Your ENTIRE response must be ONLY a valid JSON object.
2. No markdown, no code fences, no explanation, no conversation.
3. If content is insufficient, use "정보 부족" for missing fields.
4. Include at least 3 key_points even if content is limited.
5. If no metrics available, set metrics to ["구체적 지표 없음"].

SPECIFICITY RULES:
1. Every key_point/claim MUST include: "구체 기술명을 특정 공정/영역에 적용하여 → 측정 가능한 수치 결과"
2. FORBIDDEN vague patterns: "활용하여 향상", "도입하여 개선", "기반한 시스템", "분석을 활용"
   REQUIRED pattern: "YOLOv8 기반 ADC를 Photo에 적용하여 결함검출률 92%→98.7%"
3. Every metric MUST be "before→after" or "X% (절대 수치)" format
4. Technology names MUST be specific (GPT-4o, Llama 3.1-70B, CNN, LSTM, Random Forest, ARIMA, YOLOv8 등)

RESPONSE FORMAT (JSON only):
{
  "title": "기사 제목을 한국어로 요약 (20자 이내)",
  "key_points": [
    "구체적인 핵심 요점 1 (수치 포함)",
    "구체적인 핵심 요점 2",
    "구체적인 핵심 요점 3",
    "구체적인 핵심 요점 4",
    "구체적인 핵심 요점 5"
  ],
  "notable_aspects": [
    "특이점/주목할 점 1",
    "특이점/주목할 점 2",
    "특이점/주목할 점 3"
  ],
  "core_highlights": "가장 중요한 핵심 포인트를 2-3문장으로 구체적으로 설명",
  "for_engineers": {
    "implementation_tasks": ["실제 필요한 작업 1", "실제 필요한 작업 2"],
    "benefits": ["기대 이점 1", "기대 이점 2"],
    "metrics": ["구체적 수치 포함 지표 1", "구체적 수치 포함 지표 2"]
  },
  "internal_lens": {
    "environment_gap": "사례 환경과 우리(내부망/DB혼재/보안제약)의 차이점",
    "production_tech": {
      "applicable_process": "Photo/Etch/CMP/박막/확산/기타 중 해당 공정",
      "yield_impact": "수율 개선 가능성 및 근거",
      "equipment_compatibility": "현재 장비와의 호환성"
    },
    "operations_tech": {
      "applicable_area": "스케줄링/레시피관리/FDC/R2R/ADC/의사결정/기타",
      "process_improvement": "개선될 운영 프로세스",
      "interface_impact": "변경될 인터페이스/절차",
      "automation_level": "무인/반자동/수동보조"
    },
    "constraint_impact": [
      "내부망으로 인한 제약사항",
      "DB 통합 문제로 인한 영향",
      "데이터 접근 제한 관련 이슈"
    ],
    "quick_wins": ["가장 쉽게 PoC 가능한 부분", "두 번째로 쉬운 적용 영역"],
    "adaptations": ["사례 대비 수정 필요 사항 1", "수정 필요 사항 2"],
    "priority_for_us": "high|medium|low",
    "priority_reason": "삼성 파운드리 관점에서의 우선순위 판단 이유"
  },
  "adoption_feasibility": {
    "difficulty": "high|medium|low",
    "difficulty_reason": "난이도 판단 이유",
    "required_resources": ["필요 인력/예산/인프라 1", "필요 자원 2"],
    "prerequisites": ["선행 조건 1", "선행 조건 2"],
    "risks": [{"risk": "위험 요소", "mitigation": "대응 방안"}],
    "roi_estimate": "ROI 추정치 (기간, 절감액 등)",
    "checklist": ["의사결정 질문 1", "의사결정 질문 2", "의사결정 질문 3"]
  },
  "milestones": {
    "total_duration_months": 12,
    "phases": [
      {"phase": "M0 준비", "duration": 1, "activities": ["활동1"], "deliverables": ["산출물1"], "gate": "Go/No-Go 기준"},
      {"phase": "M1 PoC", "duration": 2, "activities": ["활동1"], "deliverables": ["산출물1"], "gate": "확산/중단 기준"},
      {"phase": "M2 Pilot", "duration": 3, "activities": ["활동1"], "deliverables": ["산출물1"], "gate": "전사확산/조건부 기준"},
      {"phase": "M3 확산", "duration": 4, "activities": ["활동1"], "deliverables": ["산출물1"], "gate": ""},
      {"phase": "M4 최적화", "duration": null, "activities": ["활동1"], "deliverables": ["산출물1"]}
    ]
  },
  "tags": ["공정명", "기술분류", "적용영역"],
  "relevance": "high|medium|low"
}"""

ANALYSIS_USER_PROMPT = """Context about our company:
{company_context}

Analyze this article:

Title: {title}
Source: {url}

Content:
{content}"""

REQUIRED_KEYWORDS = [
    "ai", "artificial intelligence", "machine learning", "deep learning",
    "llm", "large language model", "neural network", "computer vision",
    "nlp", "generative", "predictive", "automation",
    "digital twin", "autonomous", "cobot", "intelligent",
    "인공지능", "AI", "머신러닝", "딥러닝", "자동화", "지능형",
]

PRIORITY_KEYWORDS = [
    "manufacturing", "semiconductor", "foundry", "fabrication",
    "production", "factory", "wafer", "chip",
    "yield", "defect", "quality", "process control",
    "MES", "FDC", "R2R", "ADC", "OEE", "PLC", "SCADA",
    "scheduling", "recipe", "supply chain",
    "제조", "반도체", "파운드리", "공정", "수율", "품질",
    "생산", "스마트팩토리", "웨이퍼",
]

METRIC_KEYWORDS = [
    "%", "percent", "productivity", "efficiency", "improved", "reduced",
    "increased", "cost saving", "ROI", "throughput", "defect rate",
    "downtime", "accuracy", "yield", "speed", "time",
    "향상", "개선", "절감", "증가", "감소", "효과", "성과",
]
