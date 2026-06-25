from datetime import datetime, timezone

LLM_PROVIDER = "opencode"
OPENCODE_SERVER_URL = "http://127.0.0.1:14097"
GITHUB_REPO_URL = "https://github.com/11qaws/ai-coding-industrial-cases.git"
GITHUB_REPO_DIR = "/home/qumin/discord/data-collector/repo"

OUTPUT_DIR = "/home/qumin/discord/data-collector/output/daily"

SEARCH_QUERIES = [
    "\"vibe coding\" manufacturing industry case study",
    "\"AI-assisted programming\" industrial application",
    "\"LLM code generation\" manufacturing enterprise",
    "generative AI software development legacy system integration",
    "conversational programming industrial security internal network",
    "바이브코딩 제조업 개발 사례",
    "AI 코딩 도구 제조 산업 현장 적용",
    "생성형 AI 레거시 시스템 마이그레이션",
    "내부망 AI 개발 도구 보안 적용 사례",
    "LLM 기반 코딩 생산성 향상 지표",
]

ANALYSIS_SYSTEM_PROMPT = """You are a technical analyst specializing in AI-assisted software development (vibe coding) in the manufacturing industry. Analyze the given article and provide a structured analysis.

IMPORTANT: Return ONLY valid JSON. No markdown, no code fences, no explanation.

{
  "title": "기사 제목 (한국어 요약)",
  "key_points": [
    "핵심 요점 1 (구체적으로)",
    "핵심 요점 2",
    "핵심 요점 3",
    "핵심 요점 4",
    "핵심 요점 5"
  ],
  "notable_aspects": [
    "특이점/주목할 점 1",
    "특이점/주목할 점 2",
    "특이점/주목할 점 3"
  ],
  "core_highlights": "가장 중요한 핵심 포인트 (2-3문장, 구체적이고 강조된 형태)",
  "for_engineers": {
    "implementation_tasks": [
      "도입에 필요한 작업 1",
      "도입에 필요한 작업 2"
    ],
    "benefits": [
      "기대 이점 1",
      "기대 이점 2"
    ],
    "metrics": [
      "구체적 성능/효과 지표 1 (숫자 포함)",
      "구체적 성능/효과 지표 2 (숫자 포함)"
    ]
  },
  "tags": ["tag1", "tag2"],
  "relevance": "high|medium|low"
}"""

ANALYSIS_USER_PROMPT = """Analyze the following article about vibe coding / AI-assisted development in the manufacturing industry:

Title: {title}
Source: {url}

Content:
{content}
"""
