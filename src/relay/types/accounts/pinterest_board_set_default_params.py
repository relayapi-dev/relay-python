# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PinterestBoardSetDefaultParams"]


class PinterestBoardSetDefaultParams(TypedDict, total=False):
    board_id: Required[str]
    """Pinterest board ID to set as default"""
