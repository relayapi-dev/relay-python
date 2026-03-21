# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AnalyticsListDailyMetricsParams"]


class AnalyticsListDailyMetricsParams(TypedDict, total=False):
    account_id: str
    """Filter by account ID"""

    from_date: str
    """Start date (ISO 8601)"""

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

    to_date: str
    """End date (ISO 8601)"""
