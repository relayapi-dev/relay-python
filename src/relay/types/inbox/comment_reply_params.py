# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommentReplyParams"]


class CommentReplyParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID to reply from"""

    text: Required[str]
    """Reply text"""

    comment_id: str
    """Parent comment ID for threaded replies"""
