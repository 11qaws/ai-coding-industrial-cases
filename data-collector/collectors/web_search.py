import sys
sys.path.insert(0, "/home/qumin/discord/data-collector")

from ddgs import DDGS
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict
import re

BLOCKED_PATTERNS = [
    "네이버 VIBE", "NAVER VIBE", "바이브 앱", "Google Play", "App Store",
    "vibe 뜻", "바이브 뜻", "느낌있죠", "TikTok", "daum", "Daum",
    "naver.com", "namu.wiki", "dictionary", "사전", "영어 사전",
    "Cambridge Dictionary", "Britannica", "RedKiwi",
    "genitive", "vibration", "음악", "music download",
    "windows store", "microsoft store", "apps on google",
]


def _is_relevant(item: dict) -> bool:
    title = item.get("title", "") + " " + item.get("body", "")
    url = item.get("href", "")
    for pat in BLOCKED_PATTERNS:
        if pat.lower() in title.lower() or pat.lower() in url.lower():
            return False
    return True


def search_duckduckgo(query: str, max_results: int = 8) -> List[Dict]:
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
            filtered = [r for r in results if _is_relevant(r)]
            for r in filtered:
                r["query"] = query
            return filtered
    except Exception as e:
        print(f"  [WARN] DuckDuckGo search failed for '{query}': {e}")
        return []


def search_all(queries: List[str], max_per_query: int = 8) -> List[Dict]:
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
                    })
    return all_results
