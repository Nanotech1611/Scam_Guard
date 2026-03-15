<p align="center">
  <h1 align="center">🛡️ Scam Guard</h1>
  <p align="center">
    LLM-powered scam & spam detection engine that classifies messages, extracts red flags, assigns risk scores, and explains its reasoning — built with LangChain &amp; Gemini for real-world scalability.
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Gemini_2.5_Flash-LLM-4285F4?logo=google&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/LangChain-Framework-1C3C3C?logo=langchain&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/Streamlit-UI-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pydantic-Validation-E92063?logo=pydantic&logoColor=white" alt="Pydantic">
</p>

---

## 📌 Problem Statement

Digital fraud is evolving faster than traditional keyword filters can adapt. Scammers now use context-aware, emotionally charged language — impersonating banks, government agencies, and telecom providers — to manipulate users into sharing OTPs, clicking phishing links, or surrendering personal data.

**Scam Guard** addresses this by leveraging **Large Language Models (LLMs)** with **LangChain orchestration** and **structured output validation** to detect, explain, and risk-score scam messages in real time — going far beyond static blacklists.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Smart Classification** | Labels messages as `Spam`, `Not Spam`, or `Uncertain` using LLM-powered prompt chains |
| 📊 **Risk Scoring** | Assigns a 0–100 risk score to each message for quantified threat assessment |
| 🚩 **Red Flag Detection** | Identifies specific suspicious elements (urgency cues, phishing URLs, fake authority) |
| 💬 **Explainable Reasoning** | Surfaces detailed reasons behind each classification — not just a verdict, but *why* |
| 📋 **Suggested Actions** | Provides actionable recommendations for the user (e.g., "Do not click links", "Report as phishing") |
| ⚡ **Real-Time Web Interface** | Paste any message into the Streamlit UI and get instant analysis |
| 📂 **Batch CSV Analysis** | Upload a CSV file and classify thousands of messages at once with batch processing |
| 🔗 **LangChain Pipeline** | Modular `Prompt → LLM → Parser` chain architecture for clean separation of concerns |
| ✅ **Structured Output Validation** | Pydantic schemas enforce strict JSON output from the LLM — no hallucinated formats |

---

## 🧱 Tech Stack

### Backend / AI

| Technology | Purpose |
|---|---|
| **Python 3.12+** | Core application logic |
| **Google Gemini 2.5 Flash** | LLM backbone for classification and reasoning |
| **LangChain** | Orchestration framework — prompt templates, chains, output parsers |
| **LangChain Google GenAI** | LangChain integration for Gemini models |
| **Pydantic** | Structured output validation & schema enforcement |

### Frontend / Interface

| Technology | Purpose |
|---|---|
| **Streamlit** | Interactive real-time web UI with tabs for single & batch analysis |

### Data & Utilities

| Technology | Purpose |
|---|---|
| **Pandas** | Dataset ingestion, batch processing, and result export |
| **python-dotenv** | Secure environment variable management |
| **tqdm** | Progress bar support for batch operations |

---

## 🧠 How It Works

Scam Guard uses a **LangChain LCEL pipeline** that chains together three components:

```
ChatPromptTemplate → ChatGoogleGenerativeAI (Gemini 2.5 Flash) → PydanticOutputParser
```

1. **Prompt Template** — A system prompt instructs the LLM to act as "ScamGuard, an expert spam detector" and enforces JSON-only responses with Pydantic format instructions.
2. **LLM Invocation** — The message is sent to Google Gemini 2.5 Flash with `temperature=0` for deterministic, consistent outputs.
3. **Structured Parsing** — The raw LLM response is parsed and validated against a strict Pydantic schema (`SpamClassification`), returning:
   - `label` — `Spam` / `Not Spam` / `Uncertain`
   - `risk_score` — Integer 0–100
   - `reasons` — List of explanatory reasons
   - `red_flags` — List of detected suspicious elements
   - `suggested_action` — Recommended user action

---

## 🗂️ Project Structure

```
Scam_Guard/
│
├── .gitignore
│
└── project_scamguard/
    │
    ├── app.py                        # Streamlit entry point (single + batch tabs)
    ├── config.py                     # API key loading, model config, paths
    ├── requirements.txt              # Python dependencies
    ├── GenAI_Batch.xlsx              # Sample batch analysis results
    ├── .gitignore                    # Project-level ignores
    │
    ├── llm/                          # LLM layer (model, prompt, parser)
    │   ├── models.py                 # Gemini LLM initialisation via LangChain
    │   ├── prompt_template.py        # ChatPromptTemplate definition
    │   └── parser.py                 # Pydantic schema + PydanticOutputParser
    │
    ├── pipeline/                     # Orchestration layer
    │   ├── chain.py                  # LCEL chain: Prompt | LLM | Parser
    │   └── wrapper.py                # classify_message() & classify_batch() functions
    │
    └── data/                         # Dataset directory (gitignored)
        └── dataset.csv               # Labelled scam/not-scam message dataset
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.12+**
- A **Google Gemini API key** ([Get one here](https://aistudio.google.com/app/apikey))

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Nanotech1611/Scam_Guard.git
cd Scam_Guard/project_scamguard

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
# Create a .env file in the project_scamguard directory:
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

### Run the App

```bash
streamlit run app.py
```

Visit **http://localhost:8501** in your browser.

---

## 🖥️ Usage

### Single Message Analysis

1. Navigate to the **"Single Message or email"** tab
2. Paste any suspicious message or email content
3. Click **"Classify"**
4. View the classification result:
   - **Label** — Spam / Not Spam / Uncertain
   - **Risk Score** — 0 to 100
   - **Reasons** — Why the model classified it this way
   - **Red Flags** — Specific suspicious patterns detected
   - **Suggested Action** — What the user should do
5. Expand **"Raw JSON"** to see the full structured output

### Batch CSV Upload

1. Navigate to the **"Batch CSV Upload"** tab
2. Upload a CSV file (the first column should contain messages to classify)
3. Click **"Run Batch Classification"**
4. View results in a table with all classification fields

---

## 📋 Output Schema

Each classification returns a validated `SpamClassification` object:

```json
{
  "label": "Spam",
  "risk_score": 85,
  "reasons": [
    "Message creates urgency to act immediately",
    "Contains suspicious link pattern",
    "Impersonates a financial institution"
  ],
  "red_flags": [
    "Urgency language: 'act now or lose access'",
    "Suspicious URL detected",
    "Request for OTP/personal information"
  ],
  "suggested_action": "Do not click any links. Report this message as phishing to your bank."
}
```

---

## 🔮 Roadmap / Extensibility

The modular design makes it straightforward to plug in new features:

- [ ] 🌐 **Multi-language support** — Detect and translate non-English messages before analysis
- [ ] 🗄️ **Threat database integration** — Cross-check URLs against PhishTank / RBI alerts
- [ ] 🔁 **Feedback learning loop** — Capture false positives to improve prompt few-shot examples
- [ ] 📈 **Risk scoring dashboard** — Visual analytics on scam trends and detection accuracy
- [ ] 🔗 **REST API** — Expose detection as an endpoint for business integration
- [ ] 🧪 **Few-shot & CoT prompting** — Add dynamic few-shot examples and Chain-of-Thought reasoning
- [ ] 📝 **Scam type categorisation** — Label messages by scam type (OTP Fraud, Phishing, Reward Scam, etc.)

---

## 💡 Key Learnings

Building Scam Guard demonstrates practical skills in:

- 🔗 **Building LangChain LCEL pipelines** with clean prompt → model → parser composition
- 🧩 **Modular AI architecture** where the LLM layer, prompt layer, and pipeline layer are independently swappable
- ✅ **Enforcing structured LLM outputs** using Pydantic schemas and LangChain's `PydanticOutputParser`
- 🧠 **Prompt engineering** for reliable, deterministic classification with zero-temperature inference
- 🚀 **Full-stack AI web app development** with Streamlit from problem to deployment
- 📊 **Batch processing patterns** using LangChain's `.batch()` for high-throughput analysis

---

## 🤝 Contributing

Contributions are welcome! Please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source. Please check the repository for license details.

---

<p align="center">Built with 🛡️ to make the internet a safer place</p>