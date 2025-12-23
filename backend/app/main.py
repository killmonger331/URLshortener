from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from .config import get_settings
from .models import ShortenRequest, ShortenResponse
from .storage import InMemoryStorage, RedisStorage, Storage, generate_code


settings = get_settings()

app = FastAPI(title="URL Shortener API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins if settings.allowed_origins else ["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

storage: Storage
if settings.redis_url:
    storage = RedisStorage(settings.redis_url)
else:
    storage = InMemoryStorage()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/shorten", response_model=ShortenResponse)
def shorten(payload: ShortenRequest) -> ShortenResponse:
    long_url = str(payload.url)

    # Create a code and ensure no collision
    for _ in range(5):
        code = generate_code()
        if not storage.exists(code):
            storage.set(code, long_url)
            short_url = f"{settings.base_url}/{code}"
            return ShortenResponse(code=code, short_url=short_url, long_url=long_url)

    raise HTTPException(status_code=500, detail="Could not generate a unique short code.")


@app.get("/{code}")
def redirect(code: str):
    url = storage.get(code)
    if not url:
        raise HTTPException(status_code=404, detail="Short code not found.")
    return RedirectResponse(url=url, status_code=307)
