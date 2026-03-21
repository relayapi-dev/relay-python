# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BookmarkRemoveParams"]


class BookmarkRemoveParams(TypedDict, total=False):
    account_id: Required[str]
    """Twitter account ID"""

    tweet_id: Required[str]
    """Tweet ID to bookmark"""
