# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FollowUnfollowParams"]


class FollowUnfollowParams(TypedDict, total=False):
    account_id: Required[str]
    """Twitter account ID"""

    target_user_id: Required[str]
    """User ID to follow"""
