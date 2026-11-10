"""Tests for the --csv input handling of markdown-table-fixer."""

import sys
from unittest.mock import patch

import pytest

import markdown_table_fixer as mtf


def _run_main(argv):
    with patch.object(sys, "argv", argv):
        mtf.main()


def test_csv_string_is_used_instead_of_sample(capsys):
    """--csv with inline CSV text must format that text, not SAMPLE_CSV."""
    _run_main(["markdown_table_fixer.py", "--csv", "x,y\n1,2"])
    out = capsys.readouterr().out
    assert "x" in out and "1" in out
    assert "Authentication" not in out


def test_csv_file_is_used_instead_of_sample(tmp_path, capsys):
    """--csv pointing at a file must format that file, not SAMPLE_CSV."""
    csv_file = tmp_path / "in.csv"
    csv_file.write_text("name,age\nada,36\n", encoding="utf-8")
    _run_main(["markdown_table_fixer.py", "--csv", str(csv_file)])
    out = capsys.readouterr().out
    assert "ada" in out
    assert "Authentication" not in out


def test_no_csv_keeps_sample_demo(capsys):
    """Without --csv the built-in sample demo output is unchanged."""
    _run_main(["markdown_table_fixer.py"])
    out = capsys.readouterr().out
    assert "Authentication" in out
