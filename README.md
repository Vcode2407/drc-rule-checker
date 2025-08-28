# DRC Rule Checker

A modular Python engine for validating layout blocks against a configurable DRC rule deck. Inspired by physical verification tools like Synopsys IC Validator and Calibre, this project simulates spacing, enclosure, and connectivity checks using structured layout data and YAML-based rule decks.

---

## 📌 Overview

This tool reads layout data from a JSON file and applies design rule checks (DRC) defined in a YAML rule deck. It identifies violations, tags severity levels, and generates a summary report. Designed for academic chip design, early-stage layout compliance, and rule deck prototyping.

---

## 🔧 Features

- ✅ Modular validation engine (`checker.py`)
- ✅ YAML-configurable rule deck with versioning
- ✅ JSON-based layout input with block metadata
- ✅ Severity tagging (Warning, Critical)
- ✅ Violation summary report (`report.txt`)
- ✅ CLI-friendly output for automation pipelines

---

## 🧪 Tech Stack

- Python 3
- YAML (rule configuration)
- JSON (layout input)
- Bash (optional for automation)

---

## 🚀 Usage

```bash
python checker.py layout.json rules.yaml
