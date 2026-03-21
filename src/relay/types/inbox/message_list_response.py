# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageListResponse", "Data"]


class Data(BaseModel):
    id: str
    """Conversation ID"""

    account_id: str
    """Account ID"""

    participant_name: str
    """Participant display name"""

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

    updated_at: datetime
    """Last updated timestamp"""

    last_message: Optional[str] = None
    """Last message text"""

    participant_avatar: Optional[str] = None
    """Participant avatar URL"""

    unread_count: Optional[float] = None
    """Unread message count"""


class MessageListResponse(BaseModel):
    data: List[Data]

    has_more: bool
    """Whether more items exist"""

    next_cursor: Optional[str] = None
    """Cursor for next page"""
