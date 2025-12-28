from __future__ import annotations

import os
from dataclasses import dataclass
from typing import List


def _split_csv(value: str) -> List[str]:
    return [v.strip() for v in value.split(",") if v.strip()]


@dataclass(frozen=True)
class Settings:
    allowed_origins: List[str]
    allowed_origin_regex: str | None
    base_url: str | None
    redis_url: str | None


def get_settings() -> Settings:
    allowed_origins_raw = os.getenv(
    "ALLOWED_ORIGINS",
    "https://ur-lshortener-zeta.vercel.app,https://ur-lshortener-git-main-richards-projects-c0a9c9b4.vercel.app,https://ur-lshortener-ma50ct7r6-richards-projects-c0a9c9b4.vercel.app,https://ur-lshortener-nr25t5yo5-richards-projects-c0a9c9b4.vercel.app,https://richard-morales.com"
)
    allowed_origin_regex = os.getenv("ALLOWED_ORIGIN_REGEX")
    base_url = os.getenv("BASE_URL")
    if base_url:
        base_url = base_url.rstrip("/")
    redis_url = os.getenv("REDIS_URL")

    return Settings(
        allowed_origins=_split_csv(allowed_origins_raw) if allowed_origins_raw else ["*"],
        allowed_origin_regex=allowed_origin_regex,
        base_url=base_url,
        redis_url=redis_url,
    )

