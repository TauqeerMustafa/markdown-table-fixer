<div align="center">

# 🚀 markdown-table-fixer

### *Smart Markdown table alignment fixer & CSV-to-Markdown converter.*

[![CI Build Status](https://img.shields.io/github/actions/workflow/status/TauqeerMustafa/markdown-table-fixer/ci.yml?branch=main&label=CI%20Build&style=for-the-badge&logo=githubactions&logoColor=white&color=2ea44f)](https://github.com/TauqeerMustafa/markdown-table-fixer/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0-success.svg?style=for-the-badge&logo=pypi&logoColor=white)](markdown_table_fixer.py)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=for-the-badge&logo=github)](CONTRIBUTING.md)

<br/>

<p align="center">
  <a href="#-why-use-markdown-table-fixer">Why markdown-table-fixer?</a> •
  <a href="#-instant-preview">Demo</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-cli-reference">CLI Reference</a> •
  <a href="#-contributing">Contributing</a> •
  <a href="#-license">License</a>
</p>

</div>

---

## 💡 Why Use `markdown-table-fixer`?

- **Perfect Alignment**: Calculates maximum column widths and formats crisp, readable Markdown tables.
- **CSV Conversion**: Converts raw CSV or TSV spreadsheets directly into GitHub-Flavored Markdown.
- **Terminal Preview**: Test and inspect table rendering in the terminal before committing.

---

## 🎬 Instant Preview

```bash
$ python markdown_table_fixer.py
============================================================
📊 FORMATTED GITHUB-FLAVORED MARKDOWN TABLE
============================================================
| Feature         | Status      | Priority |
| --------------- | ----------- | -------- |
| Authentication  | Completed   | High     |
| Payment Gateway | In Progress | Critical |
| Dark Mode       | Planned     | Medium   |
============================================================
```

---

## ⚡ Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/TauqeerMustafa/markdown-table-fixer.git
cd markdown-table-fixer

# 2. Run CLI tool immediately (No pip install required)
python markdown_table_fixer.py --help
```

---

## 🏛️ Architecture & Workflow

```mermaid
flowchart LR
    UnevenTable["📊 Uneven Markdown / CSV Data"] --> TableFixer["⚙️ markdown_table_fixer.py"]
    TableFixer --> WidthCalc["📏 Column Width Calculation"]
    WidthCalc --> FormattedTable["✨ Aligned GitHub-Flavored Table"]
```

---

## 💻 CLI Reference

| Command | Description |
| :--- | :--- |
| `python markdown_table_fixer.py --help` | Display full help menu and flag options |
| `python markdown_table_fixer.py` | Run default execution mode |

---

## 🤝 Contributing

Contributions, feature suggestions, and pull requests are warmly welcomed!
- Read our [Contributing Guidelines](CONTRIBUTING.md).
- Follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

<div align="center">
  <sub>Crafted with ❤️ for the open-source community by <a href="https://github.com/TauqeerMustafa">Tauqeer Mustafa</a>.</sub>
</div>
