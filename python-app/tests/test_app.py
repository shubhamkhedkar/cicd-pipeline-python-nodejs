import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import create_app  # noqa: E402


def client():
    return create_app().test_client()


def test_health():
    r = client().get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_greet_default():
    assert client().get("/api/greet").get_json()["message"] == "Hello, world!"


def test_greet_name():
    r = client().get("/api/greet?name=Shubham")
    assert r.get_json()["message"] == "Hello, Shubham!"
