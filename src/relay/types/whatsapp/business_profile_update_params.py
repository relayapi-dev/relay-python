# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["BusinessProfileUpdateParams"]


class BusinessProfileUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """WhatsApp account ID"""

    about: str

    address: str

    description: str

    email: str

    websites: SequenceNotStr[str]
