import sys
sys.path.insert(0, "/home/qumin/discord/data-collector")

from ddgs import DDGS
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict
import re

from config import REQUIRED_KEYWORDS, PRIORITY_KEYWORDS, METRIC_KEYWORDS

BLOCKED_PATTERNS = [
    "네이버 VIBE", "NAVER VIBE", "바이브 앱", "Google Play", "App Store",
    "vibe 뜻", "바이브 뜻", "느낌있죠", "TikTok", "daum", "Daum",
    "naver.com", "namu.wiki", "dictionary", "영어 사전",
    "Cambridge Dictionary", "Britannica", "RedKiwi",
    "genitive", "vibration", "음악", "music download",
    "windows store", "microsoft store",
    "youtube", "instagram", "facebook",
]


def _relevance_score(text: str) -> int:
    text_lower = text.lower()
    score = 0

    has_ai = any(kw.lower() in text_lower for kw in REQUIRED_KEYWORDS)
    if not has_ai:
        return -1

    for kw in PRIORITY_KEYWORDS:
        if kw.lower() in text_lower:
            score += 2

    for kw in METRIC_KEYWORDS:
        if kw.lower() in text_lower:
            score += 1

    return score


def _is_relevant(item: dict) -> bool:
    title = item.get("title", "")
    snippet = item.get("body", "")
    url = item.get("href", "")
    combined = title + " " + snippet

    for pat in BLOCKED_PATTERNS:
        if pat.lower() in combined.lower() or pat.lower() in url.lower():
            return False

    score = _relevance_score(combined)
    return score >= 0


def search_duckduckgo(query: str, max_results: int = 10) -> List[Dict]:
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
            scored = []
            for r in results:
                combined = r.get("title", "") + " " + r.get("body", "")
                score = _relevance_score(combined)
                if score < 0:
                    continue
                if not _is_relevant(r):
                    continue
                r["query"] = query
                r["score"] = score
                scored.append(r)
            scored.sort(key=lambda x: x["score"], reverse=True)
            return scored[:5]
    except Exception as e:
        print(f"  [WARN] DuckDuckGo search failed for '{query}': {e}")
        return []


def search_all(queries: List[str], max_per_query: int = 10) -> List[Dict]:
    all_results = []
    seen_urls = set()
    with ThreadPoolExecutor(max_workers=6) as ex:
        futures = {ex.submit(search_duckduckgo, q, max_per_query): q for q in queries}
        for f in as_completed(futures):
            for r in f.result():
                url = r.get("href", "")
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    all_results.append({
                        "title": r.get("title", ""),
                        "url": url,
                        "snippet": r.get("body", ""),
                        "source": "web",
                        "query": r.get("query", ""),
                        "score": r.get("score", 0),
                    })
    all_results.sort(key=lambda x: x["score"], reverse=True)
    return all_results
