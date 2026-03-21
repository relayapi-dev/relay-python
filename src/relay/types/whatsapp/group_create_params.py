# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["GroupCreateParams"]


class GroupCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """WhatsApp account ID"""

    name: Required[str]
    """Group name"""

    contact_ids: SequenceNotStr[str]
    """Initial contact IDs"""

    description: str
    """Group description"""
