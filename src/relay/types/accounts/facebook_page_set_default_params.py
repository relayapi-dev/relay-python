# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FacebookPageSetDefaultParams"]


class FacebookPageSetDefaultParams(TypedDict, total=False):
    page_id: Required[str]
    """Facebook page ID to set as default"""
