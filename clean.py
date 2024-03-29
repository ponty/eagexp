#!/usr/bin/env python3
import pathlib, shutil

[shutil.rmtree(p) for p in pathlib.Path(".").glob(".mypy_cache")]
[shutil.rmtree(p) for p in pathlib.Path(".").glob(".pytest_cache")]
[shutil.rmtree(p) for p in pathlib.Path(".").glob(".tox")]
[shutil.rmtree(p) for p in pathlib.Path(".").glob("dist")]
[shutil.rmtree(p) for p in pathlib.Path(".").glob("*.egg-info")]
[shutil.rmtree(p) for p in pathlib.Path(".").glob("build")]
[p.unlink() for p in pathlib.Path(".").rglob("*.py[co]")]
[p.rmdir() for p in pathlib.Path(".").rglob("__pycache__")]
[p.unlink() for p in pathlib.Path(".").rglob("*.log")]
