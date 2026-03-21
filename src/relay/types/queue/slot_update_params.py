# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["SlotUpdateParams", "Slot"]


class SlotUpdateParams(TypedDict, total=False):
    name: str
    """Schedule name"""

    set_as_default: bool
    """Set this schedule as the default"""

    slots: Iterable[Slot]
    """Updated time slots"""


class Slot(TypedDict, total=False):
    day_of_week: Required[int]
    """Day of week (0=Sunday, 6=Saturday)"""

    time: Required[str]
    """Time in HH:MM format"""

    timezone: Required[str]
    """IANA timezone (e.g. America/New_York)"""
