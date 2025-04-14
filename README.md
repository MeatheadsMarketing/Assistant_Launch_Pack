# Assistant Launch Pack

This is a complete modular assistant orchestration platform built from `v1.1` to `v1.6`, structured to support assistant development, deployment, monetization, and automation.

---

## ✅ Versions

- **v1.1**: Tab loader + Streamlit baseline
- **v1.2**: Validator system + launch scaffolds
- **v1.3**: Feedback logging + token tracking
- **v1.4**: Flow orchestration + session logic
- **v1.5**: Assistant dashboard + monetization + packaging
- **v1.6**: API + deployable services (prepped)

---

## 📁 Structure

Each version folder contains:
- `run_ui.py` – main launcher
- `tabs/` – assistant interfaces
- `agent_registry.json` – metadata
- `audit/`, `handoffs/`, `idea_log/` – system state logs

---

## 🚀 How to Run

```bash
cd v1.5
python3 -m venv ../.venv
source ../.venv/bin/activate
pip install -r requirements.txt
streamlit run run_ui.py
```

---

## 🔒 Licensing

Custom or commercial licensing available on request.
