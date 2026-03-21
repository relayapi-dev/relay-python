# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ReviewListResponse", "Data"]


class Data(BaseModel):
    id: str
    """Review ID"""

    author_name: str
    """Review author name"""

    created_at: datetime
    """Review timestamp"""

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

    rating: float
    """Rating (1-5)"""

    reply: Optional[str] = None
    """Business reply text"""

    text: Optional[str] = None
    """Review text"""


class ReviewListResponse(BaseModel):
    data: List[Data]

    has_more: bool
    """Whether more items exist"""

    next_cursor: Optional[str] = None
    """Cursor for next page"""
