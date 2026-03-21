# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HealthListResponse", "Data", "DataError"]


class DataError(BaseModel):
    code: str

    message: str


class Data(BaseModel):
    id: str

    healthy: bool

    platform: Literal[
        "twitter",
        "instagram",
        "facebook",
        "linkedin",
        "tiktok",
        "youtube",
        "pinterest",
        "reddit",
        "bluesky",
        "threads",
        "telegram",
        "snapchat",
        "googlebusiness",
        "whatsapp",
        "mastodon",
        "discord",
        "sms",
    ]

    token_expires_at: Optional[datetime] = None

    username: Optional[str] = None

    error: Optional[DataError] = None


class HealthListResponse(BaseModel):
    data: List[Data]
