# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RedditGetFeedParams"]


class RedditGetFeedParams(TypedDict, total=False):
    account_id: Required[str]
    """Reddit account ID"""

    subreddit: Required[str]
    """Subreddit name"""

    cursor: str
    """Pagination cursor"""

    limit: int
    """Number of items per page"""

    sort: Literal["hot", "new", "top", "rising"]
    """Sort order"""

    time: Literal["hour", "day", "week", "month", "year", "all"]
    """Time filter (for top sort)"""
