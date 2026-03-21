# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommentPrivateReplyParams"]


class CommentPrivateReplyParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID to reply from"""

    text: Required[str]
    """Private reply text"""
