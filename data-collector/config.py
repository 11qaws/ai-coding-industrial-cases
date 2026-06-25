from datetime import datetime, timezone

LLM_PROVIDER = "opencode"
OPENCODE_SERVER_URL = "http://127.0.0.1:14097"
GITHUB_REPO_URL = "https://github.com/11qaws/ai-coding-industrial-cases.git"
GITHUB_REPO_DIR = "/home/qumin/discord/data-collector/repo"

OUTPUT_DIR = "/home/qumin/discord/data-collector/output/daily"

SEARCH_QUERIES = [
    "AI manufacturing case study productivity improvement percent",
    "LLM manufacturing quality control defect reduction results",
    "machine learning production line optimization efficiency gain",
    "AI predictive maintenance manufacturing cost savings metrics",
    "deep learning industrial automation throughput increase",
    "computer vision manufacturing inspection accuracy rate",
    "AI supply chain manufacturing inventory reduction results",
    "\"generative AI\" \"manufacturing\" productivity case study",
    "\"industrial AI\" implementation results production management",
    "Siemens Azure AI manufacturing digital twin results",
    "PLC AI programming manufacturing efficiency case study",
    "\"smart manufacturing\" AI adoption ROI metrics",
    "제조업 AI 도입 생산성 향상 사례",
    "AI 스마트팩토리 불량률 개선 효과",
    "제조 현장 AI 품질관리 도입 성과 지표",
    "AI 제조공정 최적화 비용 절감 사례",
    "LLM 제조업 적용 코드 생성 생산성",
    "AI 생산관리 시스템 도입 효과 측정",
    "제조 AI 도입 장애물 극복 사례 연구",
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

REQUIRED_KEYWORDS = [
    "ai", "artificial intelligence", "machine learning", "deep learning",
    "llm", "large language model", "neural network", "computer vision",
    "natural language processing", "generative ai", "predictive",
    "automation", "intelligent", "cobot", "autonomous",
    "인공지능", "AI", "머신러닝", "딥러닝", "자동화",
]

PRIORITY_KEYWORDS = [
    "manufacturing", "production", "factory", "industrial", "assembly line",
    "supply chain", "quality control", "predictive maintenance", "PLC",
    "manufacturing execution", "MES", "ERP", "SCADA", "IoT",
    "제조업", "생산", "공장", "스마트팩토리", "품질",
    "생산관리", "제조", "설비",
]

METRIC_KEYWORDS = [
    "%", "percent", "productivity", "efficiency", "improved", "reduced",
    "increased", "cost saving", "ROI", "throughput", "defect rate",
    "downtime", "accuracy", "speed", "time",
    "향상", "개선", "절감", "증가", "감소", "효과", "성과", "%",
]
