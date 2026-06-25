import sys
sys.path.insert(0, "/home/qumin/discord/data-collector")

import requests
from bs4 import BeautifulSoup
from typing import Optional
from urllib.parse import urlparse


def fetch_page(url: str, max_chars: int = 8000) -> Optional[str]:
    try:
        parsed = urlparse(url)
        if "arxiv.org" in parsed.netloc:
            abs_url = url.replace("/abs/", "/abs/") if "/abs/" in url else url
            return f"[arXiv paper: {abs_url}]"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()
        text = soup.get_text(separator="\n", strip=True)
        lines = [l for l in text.split("\n") if len(l.strip()) > 40]
        clean = "\n".join(lines)
        return clean[:max_chars] if len(clean) > max_chars else clean
    except Exception as e:
        print(f"  [WARN] Failed to fetch {url}: {e}")
        return None
