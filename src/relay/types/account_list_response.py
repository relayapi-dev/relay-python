# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountListResponse", "Data"]


class Data(BaseModel):
    id: str
    """Account ID"""

    avatar_url: Optional[str] = None

    connected_at: datetime

    display_name: Optional[str] = None

    metadata: Optional[Dict[str, Optional[object]]] = None

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

    platform_account_id: str

    updated_at: datetime

    username: Optional[str] = None


class AccountListResponse(BaseModel):
    data: List[Data]

    has_more: bool
    """Whether more items exist"""

    next_cursor: Optional[str] = None
    """Cursor for next page"""
