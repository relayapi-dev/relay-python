# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContactListParams"]


class ContactListParams(TypedDict, total=False):
    account_id: Required[str]
    """WhatsApp account ID"""

    cursor: str
    """Pagination cursor"""

    limit: int
    """Number of items"""

    search: str
    """Search by name or phone"""

    tag: str
    """Filter by tag"""
