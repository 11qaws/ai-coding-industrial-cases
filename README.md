# AI Coding Industrial Cases

**목적:** 삼성전자 DS 파운드리사업부 관점에서 제조업/반도체 AI 도입 사례를 수집하고, 내부 엔지니어가 실행 가능한 인사이트로 가공합니다.

## 시스템 구성

```
discord/
├── data-collector/      # System 1: 데이터 수집 및 1차 분석
│   ├── main.py          # 오케스트레이터 (매일 03:00 cron 실행)
│   ├── config.py        # 검색어, 회사 컨텍스트, LLM 프롬프트
│   ├── collectors/      # DuckDuckGo + ArXiv 검색 + 스크래핑
│   ├── llm/             # LLM 추상화 (opencode / OpenAI / Anthropic)
│   ├── reporters/       # 마크다운 리포트 생성
│   └── output/daily/    # 일일 리포트 저장소
│
├── deep-analyzer/       # System 2: 심층 분석 (별도 환경에서 실행 가능)
│   ├── main.py          # 오케스트레이터 (매일 05:00 cron 실행)
│   ├── config.py        # 분석 프롬프트, 회사 컨텍스트
│   ├── analyzers/       # 패턴/인사이트, 기술 심층, 주간 종합 분석
│   ├── llm/             # System 1과 동일한 LLM 추상화
│   ├── reporters/       # 확장된 리포트 포맷
│   └── output/          # insights/, deepdive/, weekly/
│
└── README.md
```

## GitHub 저장소 구조

```
ai-coding-industrial-cases/
├── daily/           ← System 1: 일일 수집 리포트
│   └── ai-coding-YYYY-MM-DD.md
├── insights/        ← System 2: 패턴/인사이트 분석
│   └── insights-YYYY-MM-DD.md
├── deepdive/        ← System 2: 기술 심층 분석
│   └── deepdive-YYYY-MM-DD.md
└── weekly/          ← System 2: 주간 종합 리포트
    └── weekly-YYYY-WW.md
```

## 회사 컨텍스트

분석은 다음 환경을 기준으로 수행됩니다:

| 항목 | 내용 |
|------|------|
| **회사** | 삼성전자 DS 부문 파운드리사업부 |
| **사업** | 반도체 웨이퍼 가공 (Foundry) |
| **경쟁사** | TSMC, Intel Foundry |
| **환경** | 국가핵심기술 → 내부망(air-gapped) 전용, 엄격한 보안 정책 |
| **제약** | 접근 불가능 데이터 다수, 여러 DB 혼재 및 DB 간 통합 미흡 |
| **IT** | 개발 친화적이지 않은 환경, 제한된 도구/인프라 |

## 분석 범위

| 영역 | 내용 |
|------|------|
| **생산 기술 (Production Tech)** | 수율(Yield) 개선, 공정 안정성, 설비 효율(OEE), 품질 불량률 감소 |
| **운영 기술 (Operations Tech)** | MES 고도화, 생산 스케줄링, FDC/R2R 자동화, 레시피 관리, ADC(자동결함분류), SOP 자동화, 의사결정 자동화, 인터페이스 통합 |

## 리포트 종류

### 1. 일일 리포트 (`daily/`)
매일 수집된 30개 기사에 대한 개별 분석.

각 기사 포함 항목:
- **Key Points** (5개+) - 구체 기술명 + 적용 공정/영역 + 수치 결과
- **Notable Aspects** (3개+) - 특이점
- **Core Highlights** - 핵심 포인트
- **For Engineers** - 도입 작업, 기대 효과, 구체적 지표
- **Internal Lens (삼성 파운드리 관점)** - 환경 차이, 생산기술/운영기술 적용 검토, 제약사항, Quick Wins, 우선순위
- **도입 가능성** - 난이도, 필요 자원, 리스크, ROI, 의사결정 체크리스트
- **실행 마일스톤** - M0 준비 → M1 PoC → M2 Pilot → M3 확산 → M4 최적화

### 2. 인사이트 리포트 (`insights/`)
누적 데이터의 패턴 분석.

- 반복 테마 (생산기술/운영기술 분류)
- 생산기술 인사이트 (적용 공정, 수율 영향)
- 운영기술 인사이트 (개선 프로세스, 자동화 수준)
- 떠오르는 트렌드 (신호 강도 포함)
- 정보 격차 및 기회
- 도입 가능성 요약

### 3. 기술 심층 리포트 (`deepdive/`)
특정 기술의 집중 분석.

- 기술 개요 (제품명/버전/방법론 포함)
- 생산 기술 적용 (공정별 적용 방안 및 기대 효과)
- 운영 기술 적용 (영역별 적용 방안 및 프로세스 변경)
- 도입 패턴, 성공 요인, 도전 과제
- 주요 지표
- 내부 배포 검토 (내부망 가능성, 데이터 요구사항, 통합 복잡도)
- 제안

### 4. 주간 종합 리포트 (`weekly/`)
일요일 생성, 경영진 보고용.

- Executive Summary (모든 문장이 "기술+적용처+결과+수치" 형식)
- 주요 발견 (중요도/영역별)
- 기술 현황 (생산기술/운영기술 분류)
- 지표 종합 (카테고리별 수치 범위)
- 도입 로드맵 (즉시/단기/중기)
- 제안 (우선순위별, ROI 포함)

## 리포트 작성 원칙

### SPECIFICITY RULES (전체 리포트 공통)

1. 모든 요점/인사이트는 반드시 **"구체 기술명을 특정 공정/영역에 적용하여 → 측정 가능한 수치 결과"** 형식
2. 금지 표현:
   - ❌ "AI를 활용하여 향상"
   - ❌ "데이터 분석 기반 시스템 도입으로 개선"
   - ❌ "딥러닝 모델을 적용하여 생산성 향상"
3. 필수 표현:
   - ✅ "CNN 기반 ADC를 Photo 공정에 적용하여 결함 검출률 92% → 98.7%"
   - ✅ "LSTM 예지보전 모델을 Etch 장비에 적용하여 downtime 37% 감소 (6.2→3.9시간/월)"
   - ✅ "YOLOv8m을 CMP 검사에 도입하여 불량 분류 속도 3.2초→0.8초, 정확도 94.5%"
4. 모든 수치는 **"before→after"** 또는 **"X% (절대 수치)"** 형태
5. 기술명은 **구체적 제품명/버전/방법론**까지 명시 (GPT-4o, Llama 3.1-70B, YOLOv8m, LSTM, ARIMA 등)

## LLM 교체

두 시스템 모두 LLM 공급자를 교체할 수 있습니다:

```python
# config.py
LLM_PROVIDER = "opencode"   # opencode 서버 API (기본)
LLM_PROVIDER = "openai"     # OpenAI API (미구현 - API 키 필요)
LLM_PROVIDER = "anthropic"  # Anthropic API (미구현 - API 키 필요)
```

## 실행 일정

| 시스템 | 시간 | 작업 | 환경 |
|--------|------|------|------|
| System 1 (Collector) | 매일 03:00 KST | 수집 + 분석 + 일일 리포트 | WSL (현재) |
| System 2 (Deep Analyzer) | 매일 05:00 KST | 심층 분석 + GitHub push | 별도 환경 가능 |

## TODO

- [ ] Email notification (메일 발송 기능)
- [ ] System 1과 System 2의 LLM 독립적 교체 테스트
- [ ] 특별 리포트: 기업 프로파일, 벤더 분석, 기술 예측
- [ ] GitHub Actions 마이그레이션 검토
