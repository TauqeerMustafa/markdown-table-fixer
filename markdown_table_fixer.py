#!/usr/bin/env python3
"""
markdown-table-fixer: Formats uneven markdown tables & converts CSV to Markdown.
"""
import argparse, csv, os, sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass

__version__ = "1.0.0"

def format_markdown_table(rows):
    if not rows:
        return ""
    col_widths = [max(len(str(row[i])) for row in rows) for i in range(len(rows[0]))]
    col_widths = [max(w, 3) for w in col_widths]
    
    lines = []
    # Header
    h = " | ".join(str(rows[0][i]).ljust(col_widths[i]) for i in range(len(rows[0])))
    lines.append(f"| {h} |")
    # Separator
    sep = " | ".join("-" * col_widths[i] for i in range(len(rows[0])))
    lines.append(f"| {sep} |")
    # Body
    for r in rows[1:]:
        row_str = " | ".join(str(r[i]).ljust(col_widths[i]) for i in range(len(r)))
        lines.append(f"| {row_str} |")
    return "\n".join(lines)

SAMPLE_CSV = """Feature,Status,Priority
Authentication,Completed,High
Payment Gateway,In Progress,Critical
Dark Mode,Planned,Medium"""

def load_csv_input(value):
    """Return rows for --csv: an existing file path is read, otherwise the
    value itself is parsed as inline CSV text."""
    if os.path.isfile(value):
        with open(value, newline="", encoding="utf-8") as f:
            return list(csv.reader(f))
    return list(csv.reader(value.splitlines()))

def main():
    parser = argparse.ArgumentParser(description="📊 markdown-table-fixer: Table formatter & CSV converter")
    parser.add_argument("--csv", help="Input CSV string or file")
    args = parser.parse_args()

    if args.csv:
        rows = load_csv_input(args.csv)
    else:
        reader = csv.reader(SAMPLE_CSV.splitlines())
        rows = list(reader)
    md_table = format_markdown_table(rows)
    
    print("=" * 60)
    print("📊 FORMATTED GITHUB-FLAVORED MARKDOWN TABLE")
    print("=" * 60)
    print(md_table)
    print("=" * 60)

if __name__ == "__main__":
    main()
