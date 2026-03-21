# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AnalyticsRetrieveParams"]


class AnalyticsRetrieveParams(TypedDict, total=False):
    account_id: str
    """Filter by account ID"""

    from_date: str
    """Start date (ISO 8601 date string)"""

    limit: int
    """Number of items"""

    offset: Optional[int]
    """Offset"""

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
    """Filter by platform"""

    post_id: str
    """Filter by post ID"""

    to_date: str
    """End date (ISO 8601 date string)"""
