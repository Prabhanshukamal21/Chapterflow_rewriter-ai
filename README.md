# Chapterflow_rewriter-ai

Automated Book Publication Workflow
Objective: Create a system to fetch content from a web URL, apply an AI-driven "spin" to chapters, allow multiple human-in-the-loop iterations, and manage content versions.

Key Capabilities:

1.Scraping & Screenshots: Fetch content and save screenshots from https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1.
2.AI Writing & Review: Use LLMs (e.g., Gemini) for chapter "spinning" by an AI Writer and refinement by an AI Reviewer.
3.Human-in-the-Loop: Facilitate multiple iterations with human input for writers, reviewers, and editors before finalization.
4.Agentic API: Ensure seamless content flow between AI agents.
5.Versioning & Consistency: Save final versions and enable consistent retrieval of published content using ChromaDB for storage and a RL search algorithm for intelligent retrieval.
Core Tools:

Python: Primary development language.
Playwright: For web scraping and screenshots.
LLM: For AI writing, reviewing, and editing.
ChromaDB: For content versioning and search.
RL Search Algorithm: For consistent data retrieval.


# 📚 chapterflow

AI-powered rewriting and version control system for chapters or documents.  
Built using **Groq + LLaMA3**, stored in **ChromaDB**, and reviewed via a **FastAPI UI**.

---

## ✨ Features

- ✍️ Rewrites chapters using **Groq's LLaMA 3** model
- 🧠 Stores AI-generated versions with **ChromaDB**
- 🧾 Allows human reviewers to submit feedback through a **web UI**
- 🗂️ Maintains metadata-rich version history
- ⚡ Fast and modular architecture (FastAPI, Gradio-compatible, etc.)

---

## 🏗️ Tech Stack

| Component        | Purpose                         |
|------------------|----------------------------------|
| 🧠 Groq / LLaMA3  | Chapter rewriting via LLM        |
| 🗃️ ChromaDB       | Vector store for versioned content |
| 🧪 FastAPI         | Backend and review submission     |
| 🖼️ Jinja2          | Templates for feedback UI         |
| 🔑 .env            | API key & config management       |


# First Run main.py then Run feedback_ui.py using python -m ui.feedback_ui
