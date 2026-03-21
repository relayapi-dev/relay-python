# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ContactCreateParams"]


class ContactCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """WhatsApp account ID"""

    phone: Required[str]
    """Phone number in E.164 format"""

    email: str
    """Email address"""

    name: str
    """Contact name"""

    tags: SequenceNotStr[str]
    """Tags"""
