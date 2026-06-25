from datetime import datetime, timezone

LLM_PROVIDER = "opencode"
OPENCODE_SERVER_URL = "http://127.0.0.1:14097"
GITHUB_REPO_URL = "https://github.com/11qaws/ai-coding-industrial-cases.git"
GITHUB_REPO_DIR = "/home/qumin/discord/data-collector/repo"

OUTPUT_DIR = "/home/qumin/discord/data-collector/output/daily"

SEARCH_QUERIES = [
    '"vibe coding" manufacturing industry case study',
    '"vibe coding" enterprise adoption security',
    '"AI-assisted programming" industrial control',
    '"LLM code generation" manufacturing enterprise',
    '"generative AI" legacy system migration manufacturing',
    '"AI coding assistant" internal network enterprise security',
    '"industrial copilot" AI development manufacturing',
    '"conversational programming" software engineering industry',
    '"AI pair programmer" enterprise deployment',
    "\"바이브 코딩\" 제조업 개발 도입",
    "AI 코딩 도구 제조 현장 보안 내부망 적용 사례",
    "생성형 AI 레거시 시스템 마이그레이션 제조",
    "LLM 기반 코딩 생산성 지표 개선 효과",
    "\"Siemens Industrial Copilot\" manufacturing",
    "PLC AI programming assistant manufacturing",
]

ANALYSIS_SYSTEM_PROMPT = """You are a technical analyst specializing in AI-assisted software development (vibe coding) in the manufacturing industry. Analyze the given article and provide a structured analysis.

ABSOLUTE RULES:
1. Your ENTIRE response must be ONLY a valid JSON object.
2. No markdown, no code fences, no explanation, no conversation.
3. If the article content is insufficient, use "정보 부족" for missing fields.
4. You MUST include at least 3 key_points even if the content is limited.
5. If no metrics are available, set metrics to ["구체적 지표 없음"].

RESPONSE FORMAT (JSON only):
{
  "title": "기사 제목을 한국어로 요약 (2-3단어 설명 포함, 20자 이내)",
  "key_points": [
    "구체적인 핵심 요점 1",
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
    "implementation_tasks": ["도입 작업 1", "도입 작업 2"],
    "benefits": ["이점 1", "이점 2"],
    "metrics": ["구체적 수치 포함 지표 1", "구체적 수치 포함 지표 2"]
  },
  "tags": ["tag1", "tag2"],
  "relevance": "high|medium|low"
}"""

ANALYSIS_USER_PROMPT = """Analyze this article:

Title: {title}
Source: {url}

Content:
{content}"""
