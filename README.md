# Web Scraping AI Agent

Scrape any public web page with a single click. The app spins up a headless browser (Playwright), streams the rendered HTML to an LLM (OpenAI GPT‑4o or Groq’s Llama‑3), and returns clean JSON—‑all wrapped in a friendly Streamlit UI.

---

## ✨ Features

| Capability           | Details                                                      |
| -------------------- | ------------------------------------------------------------ |
| **One‑click scrape** | Paste a URL, describe what you need, hit **Scrape**.         |
| **Autonomous agent** | SmartScraperGraph decides *how* to fetch, parse and extract. |
| **Headless browser** | Playwright renders JS‑heavy sites before extraction.         |
| **Model choice**     | Select GPT‑4o, GPT‑3.5‑turbo, Groq Llama‑3, etc.             |
| **Streamlit UX**     | Runs locally on `localhost:8501`; no setup beyond Python.    |
| **JSON‑only output** | Pydantic schema enforcement means ready‑to‑use data.         |

---

## 🛠 Tech Stack

* **Python 3.11**
* [Streamlit](https://streamlit.io) for the web UI
* [Playwright](https://playwright.dev) for browser automation
* [ScrapeGraphAI](https://github.com/VisionSystemsInc/scrapegraphai) for agent logic
* **OpenAI / Groq** LLMs for reasoning
* Optional **Ollama** embeddings for cost savings

---

## 🚀 Quick start

```bash
# 1 – Clone & enter project
git clone https://github.com/your‑org/web‑scraping‑ai‑agent.git
cd web‑scraping‑ai‑agent

# 2 – Create and activate a virtual‑env
python -m venv .venv && source .venv/bin/activate

# 3 – Install requirements
pip install -r requirements.txt
playwright install

# 4 – Set your OpenAI (or Groq) key
export OPENAI_API_KEY="<your‑key>"
#   or
export GROQ_API_KEY="<your‑key>"

# 5 – (Opt.) run local embeddings to cut token cost
ollama run nomic-embed-text &

# 6 – Launch the app
streamlit run web_scraper.py
```


---

## ⚙️ Configuration

| Variable                           | Purpose                                       |
| ---------------------------------- | --------------------------------------------- |
| `OPENAI_API_KEY`                   | Auth key for the chosen LLM provider.         |
| `MODEL_NAME`                       | Override default model (e.g., `gpt-4o-mini`). |
| `EMBEDDINGS_BASE_URL`              | Point to a local Ollama instance.             |

All env vars can be placed in a `.env` file (auto‑read by `python‑dotenv`).

---

## 📂 Project Structure

```
├── web_scraper.py          # Streamlit entry‑point
├── requirements.txt        # Locked dependencies
├── README.md               # You are here 🙌
└── …
```

---






