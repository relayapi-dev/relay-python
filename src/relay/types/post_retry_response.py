# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PostRetryResponse", "Media", "Targets", "TargetsAccount", "TargetsError"]


class Media(BaseModel):
    url: str
    """Public URL of the media file"""

    type: Optional[Literal["image", "video", "gif", "document"]] = None
    """Media type. Inferred from URL extension if omitted."""


class TargetsAccount(BaseModel):
    id: str

    url: Optional[str] = None
    """Published post URL on the platform"""

    username: Optional[str] = None


class TargetsError(BaseModel):
    code: str

    message: str


class Targets(BaseModel):
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

    status: Literal["draft", "scheduled", "publishing", "published", "failed"]

    accounts: Optional[List[TargetsAccount]] = None

    error: Optional[TargetsError] = None


class PostRetryResponse(BaseModel):
    id: str
    """Post ID"""

    content: Optional[str] = None

    created_at: datetime

    media: Optional[List[Media]] = None

    scheduled_at: Optional[str] = None

    status: Literal["draft", "scheduled", "publishing", "published", "failed", "partial"]

    targets: Dict[str, Targets]
    """Per-target results"""

    updated_at: datetime
