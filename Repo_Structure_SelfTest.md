# Assistant Launch Pack – Repo Structure Self-Test

Use this checklist to visually verify that your folder and file structure is correct across all versions (v1.1 to v1.6).

---

## ✅ Expected Top-Level Layout

```
Assistant_Launch_Pack/
├── v1.1/
├── v1.2/
├── v1.3/
├── v1.4/
├── v1.5/
├── v1.6/
├── README.md
├── logs/                     # optional (feedback, token, audit)
└── .venv/                    # optional (for local virtual environment)
```

---

## ✅ Inside Any Version Folder (Example: v1.5)

```
v1.5/
├── run_ui.py
├── version_manifest.json
├── agent_registry.json
├── agent_status.py
├── monetization_tags.py
├── assistant_packager.py
├── pricing_tiers.json
├── launch_checklist.md
├── tabs/
│   ├── tab_agent_dashboard.py
│   ├── filter_panel.py
│   └── (other functional tabs)
├── packs/
│   └── assistant_pack_*.zip
├── audit/
│   ├── v1.5_final_audit.md
│   └── v1.5_final_audit.json
├── handoffs/
│   └── v1.5_clarity_handoff.md
└── idea_log/
    └── v1.6_idea_log.md
```

---

## ✅ Visual Self-Test Checklist

| Item | Visual Check | Notes |
|------|---------------|-------|
| [ ] `run_ui.py` present and launchable | |
| [ ] `/tabs/` has functional tabs (`dashboard`, `filter`, etc.) | |
| [ ] `agent_registry.json` contains agents with `tags` + `tier` | |
| [ ] `agent_status.py` works with `agent_status.json` | |
| [ ] `assistant_packager.py` exports valid ZIPs | |
| [ ] `pricing_tiers.json` includes Free / Pro / Enterprise | |
| [ ] `version_manifest.json` accurately reflects the files | |
| [ ] `/audit/` folder contains final audit results | |
| [ ] `/handoffs/` folder has clarity handoff doc | |
| [ ] `/idea_log/` includes `v1.6_idea_log.md` | |
| [ ] Optional: `/packs/` exists with 1+ generated assistant bundles | |

---

## ✅ When Done

Send a folder scaffold (screenshot or text tree) so we can run final validation.

