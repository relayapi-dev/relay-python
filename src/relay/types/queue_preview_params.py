# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["QueuePreviewParams"]


class QueuePreviewParams(TypedDict, total=False):
    count: int
    """Number of upcoming slots to preview"""
