# 🔧 File: main.py
import sys
import os
sys.path.append(os.path.abspath("."))
from Scraper.scraper import scrape_chapter
from agents.writer import rewrite_chapter
from Storage.chroma_utils import add_version


if __name__ == "__main__":
    print("🕸️ Scraping original chapter...")
    raw = scrape_chapter()

    print("✍️ Rewriting chapter using AI...")
    spun = rewrite_chapter(raw)

    print("🧠 Storing AI version in ChromaDB...")
    add_version("ai_writer_v1", spun, {"stage": "ai-written"})

    print("🚀 Done. Run the feedback UI for human review.")