# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ValidateValidatePostParams", "Media"]


class ValidateValidatePostParams(TypedDict, total=False):
    scheduled_at: Required[str]
    """Publish intent.

    Use "now" to publish immediately, "draft" to save as draft, or an ISO 8601
    timestamp to schedule.
    """

    targets: Required[SequenceNotStr[str]]
    """Account IDs or platform names to publish to"""

    content: str
    """Post text. Optional if target_options provide per-target content."""

    media: Iterable[Media]
    """Media attachments"""

    target_options: Dict[str, Dict[str, Optional[object]]]
    """Per-target customizations keyed by target value (account ID or platform name)"""

    timezone: str
    """IANA timezone for scheduling"""


class Media(TypedDict, total=False):
    url: Required[str]
    """Public URL of the media file"""

    type: Literal["image", "video", "gif", "document"]
    """Media type. Inferred from URL extension if omitted."""
