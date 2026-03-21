# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ContactBulkOperationsParams"]


class ContactBulkOperationsParams(TypedDict, total=False):
    account_id: Required[str]
    """WhatsApp account ID"""

    action: Required[Literal["add_tags", "remove_tags", "delete"]]
    """Action"""

    contact_ids: Required[SequenceNotStr[str]]
    """Contact IDs"""

    tags: SequenceNotStr[str]
    """Tags (for tag actions)"""
