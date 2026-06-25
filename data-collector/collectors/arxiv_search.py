import sys
sys.path.insert(0, "/home/qumin/discord/data-collector")

import arxiv
from typing import List, Dict

from config import REQUIRED_KEYWORDS, PRIORITY_KEYWORDS, METRIC_KEYWORDS


def _relevance_score(text: str) -> int:
    text_lower = text.lower()
    has_ai = any(kw.lower() in text_lower for kw in REQUIRED_KEYWORDS)
    if not has_ai:
        return -1
    score = 0
    for kw in PRIORITY_KEYWORDS:
        if kw.lower() in text_lower:
            score += 2
    for kw in METRIC_KEYWORDS:
        if kw.lower() in text_lower:
            score += 1
    return score


def search_arxiv(queries: List[str], max_results: int = 5) -> List[Dict]:
    all_results = []
    seen_ids = set()
    client = arxiv.Client()
    for q in queries:
        try:
            search = arxiv.Search(query=q, max_results=max_results, sort_by=arxiv.SortCriterion.Relevance)
            for paper in client.results(search):
                paper_id = paper.entry_id
                if paper_id in seen_ids:
                    continue
                seen_ids.add(paper_id)
                combined = paper.title + " " + paper.summary[:500]
                score = _relevance_score(combined)
                if score < 0:
                    continue
                all_results.append({
                    "title": paper.title,
                    "url": paper.entry_id,
                    "snippet": paper.summary[:500],
                    "source": "arxiv",
                    "query": q,
                    "score": score,
                })
        except Exception as e:
            print(f"  [WARN] ArXiv search failed for '{q}': {e}")
    all_results.sort(key=lambda x: x["score"], reverse=True)
    return all_results
