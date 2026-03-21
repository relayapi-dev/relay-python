# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PageSelectParams"]


class PageSelectParams(TypedDict, total=False):
    connect_token: Required[str]
    """Token from pending data or OAuth flow"""

    page_id: Required[str]
    """Selected Facebook page ID"""
