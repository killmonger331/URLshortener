from __future__ import annotations

import secrets
import string
from dataclasses import dataclass
from typing import Optional, Protocol

import redis


ALPHABET = string.ascii_letters + string.digits


def generate_code(length: int = 7) -> str:
    # 62^7 is huge; collisions are extremely unlikely, but we still check before storing.
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


class Storage(Protocol):
    def get(self, code: str) -> Optional[str]:
        ...

    def set(self, code: str, url: str) -> None:
        ...

    def exists(self, code: str) -> bool:
        ...


@dataclass
class InMemoryStorage:
    _data: dict[str, str]

    def __init__(self) -> None:
        self._data = {}

    def get(self, code: str) -> Optional[str]:
        return self._data.get(code)

    def set(self, code: str, url: str) -> None:
        self._data[code] = url

    def exists(self, code: str) -> bool:
        return code in self._data


class RedisStorage:
    def __init__(self, redis_url: str) -> None:
        # decode_responses=True returns str instead of bytes
        self._r = redis.Redis.from_url(redis_url, decode_responses=True)

    def get(self, code: str) -> Optional[str]:
        return self._r.get(code)

    def set(self, code: str, url: str) -> None:
        self._r.set(code, url)

    def exists(self, code: str) -> bool:
        return self._r.exists(code) == 1
