"""
Streamlit Web-Scraping AI Agent (OpenAI)
---------------------------------------
Scrape any public web page with **ScrapeGraphAI** using OpenAI’s GPT‑4o family
for reasoning and local Ollama embeddings for semantic search.

Quick start
-----------
1.  Activate your virtual‑env and install deps:
       pip install streamlit scrapegraphai openai pydantic langchain-openai
       playwright install

2.  Add your OpenAI key to the environment:
       export OPENAI_API_KEY="<your-key>"
       
3.  (Optional) run local embeddings (keeps costs down):
       ollama run nomic-embed-text &

4.  Launch the app:
       streamlit run streamlit_openai_scraper.py
"""

from __future__ import annotations
import os
import streamlit as st
from pydantic import BaseModel
from scrapegraphai.graphs import SmartScraperGraph

################################################################################
# Pydantic schema – defines the exact JSON we want
################################################################################
class ProductDetails(BaseModel):
    title: str
    price: str | None
    rating: float | None
    bullets: list[str] | None

################################################################################
# Config builder – OpenAI backend, JSON-only mode
################################################################################

def build_graph_config(*, model: str = "gpt-4o-mini") -> dict:
    return {
        "llm": {
            "model_provider": "openai",
            "model": model,
            "temperature": 0,
            "api_key": os.getenv("OPENAI_API_KEY"),
            # GPT‑4o supports the OpenAI JSON mode
            "response_format": {"type": "json_object"},
            "max_tokens": 2048,
        },
        "embeddings": {
            "model_provider": "ollama",
            "model": "nomic-embed-text",
            "base_url": "http://localhost:11434",
        },
        "text_splitter_kwargs": {  # keep each chunk small for pricing & speed
            "chunk_size": 3_000,
            "chunk_overlap": 0,
        },
        "verbose": True,
    }

################################################################################
# Streamlit UI
################################################################################

st.set_page_config(page_title="Web‑Scraper AI Agent (OpenAI)", page_icon="🕵️‍♂️")

st.title("Web‑Scraper AI Agent 🕵️‍♂️ – OpenAI")
st.caption("Scrape any webpage using GPT‑4o and local Ollama embeddings")

if "OPENAI_API_KEY" not in os.environ:
    st.sidebar.warning("OPENAI_API_KEY environment variable is not set – requests will fail.")

url = st.text_input("Website URL to scrape")

default_prompt = (
    "Extract the following fields and return ONLY a JSON object that matches the schema.\n"
    "If a value is unknown, use null. Do NOT write NA.\n\n"
    "Fields: title, price, rating, first 5 bullets under 'About this item'."
)
user_prompt = st.text_area("Extraction instructions", value=default_prompt, height=110)

model_choice = st.selectbox(
    "OpenAI model",
    ["gpt-4o-mini", "gpt-4o", "gpt-4o-128k", "gpt-4-turbo"],
    index=0,
)

################################################################################
# Scrape button handler
################################################################################

if st.button("Scrape"):
    if not url.strip():
        st.error("Please provide a URL to scrape.")
        st.stop()

    graph = SmartScraperGraph(
        prompt=user_prompt,
        source=url.strip(),
        config=build_graph_config(model=model_choice),
        schema=ProductDetails,
    )

    with st.spinner("Scraping…"):
        try:
            result = graph.run()
        except Exception as err:
            st.exception(err)
        else:
            st.success("Done! Parsed product details:")
            st.json(result)
