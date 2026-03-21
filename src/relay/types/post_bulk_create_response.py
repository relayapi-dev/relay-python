# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "PostBulkCreateResponse",
    "Data",
    "DataMedia",
    "DataTargets",
    "DataTargetsAccount",
    "DataTargetsError",
    "Summary",
]


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


class Summary(BaseModel):
    failed: float

    succeeded: float

    total: float


class PostBulkCreateResponse(BaseModel):
    data: List[Data]

    summary: Summary
