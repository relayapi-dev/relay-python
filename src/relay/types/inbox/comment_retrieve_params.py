# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CommentRetrieveParams"]


class CommentRetrieveParams(TypedDict, total=False):
    account_id: str
    """Filter by account ID"""

    cursor: str
    """Pagination cursor"""

    limit: int
    """Number of items"""

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
