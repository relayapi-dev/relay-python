# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BoardSelectParams"]


class BoardSelectParams(TypedDict, total=False):
    board_id: Required[str]
    """Selected Pinterest board ID"""

    connect_token: Required[str]
    """Token from pending data or OAuth flow"""
