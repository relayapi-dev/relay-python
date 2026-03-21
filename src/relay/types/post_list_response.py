# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PostListResponse", "Data", "DataMedia", "DataTargets", "DataTargetsAccount", "DataTargetsError"]


class DataMedia(BaseModel):
    url: str
    """Public URL of the media file"""

    type: Optional[Literal["image", "video", "gif", "document"]] = None
    """Media type. Inferred from URL extension if omitted."""


class DataTargetsAccount(BaseModel):
    id: str

    url: Optional[str] = None
    """Published post URL on the platform"""

    username: Optional[str] = None


class DataTargetsError(BaseModel):
    code: str

    message: str


class DataTargets(BaseModel):
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

    accounts: Optional[List[DataTargetsAccount]] = None

    error: Optional[DataTargetsError] = None


class Data(BaseModel):
    id: str
    """Post ID"""

    content: Optional[str] = None

    created_at: datetime

    media: Optional[List[DataMedia]] = None

    scheduled_at: Optional[str] = None

    status: Literal["draft", "scheduled", "publishing", "published", "failed", "partial"]

    targets: Dict[str, DataTargets]
    """Per-target results"""

    updated_at: datetime


class PostListResponse(BaseModel):
    data: List[Data]

    has_more: bool
    """Whether more items exist"""

    next_cursor: Optional[str] = None
    """Cursor for next page"""
