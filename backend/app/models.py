from __future__ import annotations

from pydantic import BaseModel, HttpUrl, Field


class ShortenRequest(BaseModel):
    url: HttpUrl


class ShortenResponse(BaseModel):
    code: str = Field(..., min_length=4, max_length=32)
    short_url: str
    long_url: str
