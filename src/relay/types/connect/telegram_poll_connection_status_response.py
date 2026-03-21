# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TelegramPollConnectionStatusResponse", "Account"]


class Account(BaseModel):
    """Connected account details"""

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


class TelegramPollConnectionStatusResponse(BaseModel):
    status: Literal["pending", "connected", "expired"]
    """Current connection status"""

    account: Optional[Account] = None
    """Connected account details"""

    chat_id: Optional[str] = None
    """Telegram chat ID once connected"""

    chat_title: Optional[str] = None
    """Chat or channel title"""

    chat_type: Optional[str] = None
    """Chat type (private, group, supergroup, channel)"""

    expires_at: Optional[datetime] = None
    """Code expiry timestamp"""
