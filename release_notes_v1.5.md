# Release Notes – Assistant Launch Pack v1.5-final

---

## 🔖 Tag: `v1.5-final`

Version `v1.5-final` introduces:
- A full **multi-agent dashboard**
- Assistant **monetization tiers**
- Filter UI, status toggling, and real-time visibility
- Assistant bundling for distribution or SaaS packaging

---

## ✅ What’s Included

### Tabs
- `tab_agent_dashboard.py` – Visual agent display, tier + tag filters, status buttons
- `filter_panel.py` – Sidebar filtering by tag and tier
- `tab_usage_log.py`, `tab_feedback_log.py`, `tab_audit_viewer.py` (from v1.3–v1.4)

### Core Modules
- `agent_registry.json` with tier metadata
- `agent_status.py` to persist status (idle, running)
- `assistant_packager.py` to zip agents by tag
- `pricing_tiers.json` with Free, Pro, Enterprise levels

---

## 📦 Packaging & Monetization

Use `assistant_packager.py` to export assistants:
- By tag (e.g., `gpt`, `seo`)
- With pricing metadata from `monetization_tags.py`

---

## 📁 Folder Snapshot
```
v1.5/
├── run_ui.py
├── tabs/
├── agent_registry.json
├── pricing_tiers.json
├── assistant_packager.py
├── audit/
├── handoffs/
├── idea_log/
```

---

## 🧪 Validation

- ✅ Level 5 Audit passed
- ✅ All files sized and executable
- ✅ Dashboard and filters tested in local run

---

## 🚀 How to Launch
```bash
cd v1.5
source ../.venv/bin/activate
streamlit run run_ui.py
```

---

## 🧠 Next Up

Self-test system for real-world clarity and log user feedback in:
`v1.6_idea_log.md`
