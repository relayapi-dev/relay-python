# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ContactImportParams", "Contact"]


class ContactImportParams(TypedDict, total=False):
    account_id: Required[str]
    """WhatsApp account ID"""

    contacts: Required[Iterable[Contact]]
    """Contacts to import"""


class Contact(TypedDict, total=False):
    phone: Required[str]
    """Phone number"""

    email: str

    name: str

    tags: SequenceNotStr[str]
