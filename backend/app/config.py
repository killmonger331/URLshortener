from __future__ import annotations

import os
from dataclasses import dataclass
from typing import List


def _split_csv(value: str) -> List[str]:
    return [v.strip() for v in value.split(",") if v.strip()]


@dataclass(frozen=True)
class Settings:
    allowed_origins: List[str]
    base_url: str
    redis_url: str | None


def get_settings() -> Settings:
    allowed_origins_raw = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")
    base_url = os.getenv("BASE_URL", "http://localhost:8000").rstrip("/")
    redis_url = os.getenv("REDIS_URL")

    return Settings(
        allowed_origins=_split_csv(allowed_origins_raw) if allowed_origins_raw else ["*"],
        base_url=base_url,
        redis_url=redis_url,
    )
