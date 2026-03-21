# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ReplyCreateParams"]


class ReplyCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    text: Required[str]
    """Reply text"""
