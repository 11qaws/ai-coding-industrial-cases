import sys
sys.path.insert(0, "/home/qumin/discord/data-collector")

from duckduckgo_search import DDGS
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict


def search_duckduckgo(query: str, max_results: int = 10) -> List[Dict]:
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
            for r in results:
                r["query"] = query
            return results
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
                    })
    return all_results
