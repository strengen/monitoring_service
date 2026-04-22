import sys
from core import run_cli


def test_cli_update(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main.py", "update"])
    run_cli()


def test_cli_add_single(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main.py", "add_single", "BookX", "15"])
    run_cli()


def test_cli_delete(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main.py", "delete_element", "BookX"])
    run_cli()