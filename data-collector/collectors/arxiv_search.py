import sys
sys.path.insert(0, "/home/qumin/discord/data-collector")

import arxiv
from typing import List, Dict


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
                all_results.append({
                    "title": paper.title,
                    "url": paper.entry_id,
                    "snippet": paper.summary[:500],
                    "source": "arxiv",
                    "query": q,
                })
        except Exception as e:
            print(f"  [WARN] ArXiv search failed for '{q}': {e}")
    return all_results
