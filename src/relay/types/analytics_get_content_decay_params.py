# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AnalyticsGetContentDecayParams"]


class AnalyticsGetContentDecayParams(TypedDict, total=False):
    post_id: Required[str]
    """Post ID to analyze decay for"""

    days: int
    """Number of days to analyze"""
