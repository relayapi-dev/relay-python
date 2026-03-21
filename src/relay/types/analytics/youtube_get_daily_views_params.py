# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["YoutubeGetDailyViewsParams"]


class YoutubeGetDailyViewsParams(TypedDict, total=False):
    account_id: Required[str]
    """YouTube account ID"""

    from_date: str
    """Start date (ISO 8601)"""

    to_date: str
    """End date (ISO 8601)"""
