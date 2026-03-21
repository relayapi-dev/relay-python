# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["AccountGroupUpdateParams"]


class AccountGroupUpdateParams(TypedDict, total=False):
    account_ids: SequenceNotStr[str]
    """Account IDs to include in the group"""

    name: str
    """Group name"""
