# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LogListParams"]


class LogListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor"""

    limit: int
    """Number of items per page"""
