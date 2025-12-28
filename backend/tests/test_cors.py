import os
import importlib
from fastapi.testclient import TestClient


def _setup_app_with_regex(regex: str):
    """Set env var and reload app.main so get_settings() picks it up."""
    os.environ["ALLOWED_ORIGIN_REGEX"] = regex
    import app.main as main_mod
    importlib.reload(main_mod)
    return main_mod.app


def test_cors_preflight_matches_regex():
    app = _setup_app_with_regex(r"https://ur-lshortener-.*\\.vercel\\.app$")
    client = TestClient(app)

    origin = "https://ur-lshortener-nr25t5yo5-richards-projects-c0a9c9b4.vercel.app"
    res = client.options(
        "/shorten",
        headers={"Origin": origin, "Access-Control-Request-Method": "POST"},
    )

    assert res.status_code in (200, 204)
    assert res.headers.get("access-control-allow-origin") == origin


def test_cors_preflight_non_matching_origin():
    app = _setup_app_with_regex(r"https://ur-lshortener-.*\\.vercel\\.app$")
    client = TestClient(app)

    origin = "https://evil.com"
    res = client.options(
        "/shorten",
        headers={"Origin": origin, "Access-Control-Request-Method": "POST"},
    )

    # When origin doesn't match the regex, the header should not be present
    assert res.headers.get("access-control-allow-origin") is None


def _setup_app_with_allowed_origins(origins: str):
    """Set env var and reload app.main so get_settings() picks it up."""
    os.environ["ALLOWED_ORIGINS"] = origins
    import app.main as main_mod
    importlib.reload(main_mod)
    return main_mod.app


def test_cors_preflight_matches_allowed_origins():
    origin = "https://ur-lshortener-nr25t5yo5-richards-projects-c0a9c9b4.vercel.app"
    app = _setup_app_with_allowed_origins(origin)
    client = TestClient(app)

    res = client.options(
        "/shorten",
        headers={"Origin": origin, "Access-Control-Request-Method": "POST"},
    )

    assert res.status_code in (200, 204)
    assert res.headers.get("access-control-allow-origin") == origin


def test_cors_preflight_non_matching_allowed_origins():
    app = _setup_app_with_allowed_origins("https://other.example")
    client = TestClient(app)

    origin = "https://evil.com"
    res = client.options(
        "/shorten",
        headers={"Origin": origin, "Access-Control-Request-Method": "POST"},
    )

    # When ALLOWED_ORIGINS does not include the origin, the header should not be present
    assert res.headers.get("access-control-allow-origin") is None
