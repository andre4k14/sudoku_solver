import sys
import pytest


# https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject/blob/main/tests/conftest.py
@pytest.fixture()
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer
