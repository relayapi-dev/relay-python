# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["SlotCreateParams", "Slot"]


class SlotCreateParams(TypedDict, total=False):
    slots: Required[Iterable[Slot]]
    """Time slots"""

    timezone: Required[str]
    """Default timezone for slots"""

    name: str
    """Schedule name"""


class Slot(TypedDict, total=False):
    day_of_week: Required[int]
    """Day of week (0=Sunday, 6=Saturday)"""

    time: Required[str]
    """Time in HH:MM format"""

    timezone: Required[str]
    """IANA timezone (e.g. America/New_York)"""
