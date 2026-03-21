# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CommentRetrieveResponse", "Data"]


class Data(BaseModel):
    id: str
    """Comment ID"""

    author_name: str
    """Comment author name"""

    created_at: datetime
    """Comment timestamp"""

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

    text: str
    """Comment text"""

    author_avatar: Optional[str] = None
    """Author avatar URL"""

    hidden: Optional[bool] = None
    """Whether comment is hidden"""

    likes: Optional[float] = None
    """Like count"""

    replies_count: Optional[float] = None
    """Reply count"""


class CommentRetrieveResponse(BaseModel):
    data: List[Data]

    has_more: Optional[bool] = None

    next_cursor: Optional[str] = None

    platform: Optional[
        Literal[
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
    ] = None

    post_id: Optional[str] = None
    """Post ID if filtered by post"""
