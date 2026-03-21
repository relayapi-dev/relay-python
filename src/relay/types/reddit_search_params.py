# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RedditSearchParams"]


class RedditSearchParams(TypedDict, total=False):
    account_id: Required[str]
    """Reddit account ID"""

    query: Required[str]
    """Search query"""

    cursor: str
    """Pagination cursor"""

    limit: int
    """Number of items per page"""

    sort: Literal["relevance", "hot", "top", "new", "comments"]
    """Sort order"""

    subreddit: str
    """Limit to subreddit"""

    time: Literal["hour", "day", "week", "month", "year", "all"]
    """Time filter"""
