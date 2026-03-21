# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AccountGroupCreateParams"]


class AccountGroupCreateParams(TypedDict, total=False):
    account_ids: Required[SequenceNotStr[str]]
    """Account IDs to include in the group"""

    name: Required[str]
    """Group name"""
