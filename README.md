# 🧪 LLM Behavioral Verification Framework

<p align="center">
  <b>Testing Large Language Models like real backend systems.</b><br/>
  Built and executed entirely on <b>Android (Termux)</b>.
</p>

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2R4aG9ndWVtbDJpM2E5NGR4b3U3Y2ZyZzF4cGQ0c3R0bWczYzF0diZlcD12MV9naWZzX3NlYXJjaCZjdD1n/13HgwGsXF0aiGY/giphy.gif" width="550"/>
</p>

---

## 🚀 What is this?

This project is a **behavioral testing & validation framework for Large Language Models (LLMs)**.

Instead of checking *exact outputs* (which fails for probabilistic systems), this framework validates **behavior**, **structure**, and **consistency** — just like production backend testing.

---

## 🧠 Why this matters

LLMs are **non-deterministic**.  
Traditional testing breaks.

This framework applies **quality engineering principles** to AI systems:

> Define expectations → Validate behavior → Detect regression

<p align="center">
  <img src="https://media.giphy.com/media/l41lUJ1YoZB1lHVPG/giphy.gif" width="520"/>
</p>

---

## 📦 Architecture Overview

Prompt Configuration (YAML) │ ▼ LLM Interface (Live / Mock) │ ▼ Response Sampler │ ▼ Validation Engine (Structure • Content • Safety) │ ▼ Step-by-Step Terminal Output │ ▼ Baseline Storage & Drift Detection

---

## ✨ Key Features

✅ Structured, machine-checkable prompts  
✅ Step-by-step validation output  
✅ Mock Mode (offline, rate-limit safe)  
✅ Live Mode (OpenAI API)  
✅ Baseline behavior storage  
✅ Regression & drift detection  
✅ Runs fully on **Android via Termux**

---

## 📱 On-Device Execution (Termux)

The entire framework was:
- Built
- Executed
- Demonstrated  

👉 **On an Android phone using Termux**

No laptop.  
No UI.  
Just Python + terminal.

<p align="center">
  <img src="https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif" width="480"/>
</p>

---

## 🧪 Step-by-Step Validation Output

Example terminal output:

[START] Baseline validation started

=== SECTION 1: DEFINITION === ✔ Structure validated

=== SECTION 2: OBJECTIVES === ✔ Required objectives present

=== SECTION 3: TEST TYPES === ✔ Positive / Negative / Boundary / Regression found

=== SECTION 4: VALIDATION CHECKS === ✔ Status codes and schema validated

=== SECTION 5: AUTOMATION === ✔ Automation logic verified

=== SECTION 6: CONCLUSION === ✔ Summary validated

[END] Baseline validation completed

This is **intentional design**, not decoration.

---

## 🛠 Tech Stack

- Python  
- OpenAI API (LLM under test)  
- YAML (prompt configuration)  
- Terminal-first execution  
- Termux (Android)

---

## ⚙️ How to Run

### 1️⃣ Clone
```bash
git clone https://github.com/vengababu-X/llm-behavior-verification.git
cd llm-behavior-verification

2️⃣ Setup

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


---

3️⃣ Mock Mode (recommended)

export LLM_MOCK=true
python -m experiments.baseline_run

✔ Offline
✔ Deterministic
✔ Demo-safe


---

4️⃣ Live Mode (OpenAI API)

export LLM_MOCK=false
export LLM_API_KEY=your_key_here
python -m experiments.baseline_run

⚠️ Subject to rate limits

```
---

📂 Project Structure

```
├── config/              # Structured prompts
├── core/                # LLM client & sampler
├── experiments/         # Baseline & regression runs
├── metrics/             # Validation logic
├── drift/               # Drift detection
├── baseline_outputs.txt # Stored baseline behavior
└── run_verification.py

```
---

🧠 Design Philosophy

LLMs are stochastic

Exact output matching fails

Behavioral validation scales


This framework validates:

What must exist

What must not change

What signals regression



---

🔮 Future Work

PASS / FAIL summary reports

CI/CD integration

Multi-model comparison

Semantic drift scoring

Coverage metrics



---

📜 License

MIT License — build, modify, extend.


---

<p align="center">
  <b>If it runs reliably on a phone, it will run anywhere.</b>
</p>
```
