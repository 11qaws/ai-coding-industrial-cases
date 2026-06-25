LLM_PROVIDER = "opencode"
OPENCODE_SERVER_URL = "http://127.0.0.1:14097"
GITHUB_REPO_URL = "https://github.com/11qaws/ai-coding-industrial-cases.git"
GITHUB_REPO_DIR = "/home/qumin/discord/deep-analyzer/repo"

INSIGHT_OUTPUT_DIR = "/home/qumin/discord/deep-analyzer/output/insights"
DEEPDIVE_OUTPUT_DIR = "/home/qumin/discord/deep-analyzer/output/deepdive"
WEEKLY_OUTPUT_DIR = "/home/qumin/discord/deep-analyzer/output/weekly"

PATTERN_SYSTEM_PROMPT = """You are a technical analyst identifying patterns and insights across multiple case studies about vibe coding / AI-assisted development in manufacturing. Synthesize the provided daily reports and extract cross-cutting insights.

IMPORTANT: Return ONLY valid JSON. No markdown, no code fences.

{
  "date": "2026-06-25",
  "total_articles_analyzed": 0,
  "recurring_themes": [
    {"theme": "테마명", "frequency": 0, "description": "설명", "examples": ["예시1", "예시2"]}
  ],
  "cross_cutting_insights": [
    {"insight": "인사이트", "evidence": "근거", "implication": "시사점"}
  ],
  "emerging_trends": [
    {"trend": "트렌드", "signal_strength": "strong|medium|weak", "details": "상세"}
  ],
  "gaps_and_opportunities": [
    {"gap": "연구/정보 격차", "opportunity": "기회 영역"}
  ]
}"""

TECHNOLOGY_DEEPDIVE_SYSTEM_PROMPT = """You are a technology analyst specializing in AI-assisted software development in manufacturing. Analyze the collected case studies and create technology deep-dives.

IMPORTANT: Return ONLY valid JSON. No markdown, no code fences.

{
  "date": "2026-06-25",
  "technologies": [
    {
      "technology": "기술명",
      "category": "LLM 도구/보안/레거시 통합/프로세스/기타",
      "case_count": 0,
      "overview": "기술 개요",
      "adoption_patterns": ["도입 패턴 1", "도입 패턴 2"],
      "success_factors": ["성공 요인 1", "성공 요인 2"],
      "challenges": ["도전 과제 1", "도전 과제 2"],
      "key_metrics": ["관련 지표 1", "관련 지표 2"],
      "recommendations": ["제안 1", "제안 2"]
    }
  ]
}"""

WEEKLY_SYSTEM_PROMPT = """You are a lead analyst creating a weekly comprehensive report on vibe coding in manufacturing. Synthesize all case studies and analyses from the past week.

IMPORTANT: Return ONLY valid JSON. No markdown, no code fences.

{
  "week": "2026-W26",
  "period": "2026-06-22 ~ 2026-06-28",
  "total_articles": 0,
  "executive_summary": "요약",
  "key_findings": [
    {"finding": "발견", "importance": "high|medium|low", "detail": "상세"}
  ],
  "technology_landscape": {
    "most_adopted": ["가장 많이 도입된 기술"],
    "emerging": ["떠오르는 기술"],
    "declining": ["주춤한 기술"]
  },
  "metrics_compilation": [
    {"category": "생산성/비용/품질/보안", "reported_values": ["value1", "value2"], "range": "범위"}
  ],
  "recommendations": [
    {"priority": "high|medium|low", "recommendation": "제안", "rationale": "근거"}
  ]
}"""
