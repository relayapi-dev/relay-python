# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PostUpdateParams", "Media"]


class PostUpdateParams(TypedDict, total=False):
    content: str
    """Post text"""

    media: Iterable[Media]
    """Updated media"""

    scheduled_at: str
    """Publish intent.

    Use "now" to publish immediately, "draft" to save as draft, or an ISO 8601
    timestamp to schedule.
    """

    target_options: Dict[str, Dict[str, Optional[object]]]

    targets: SequenceNotStr[str]
    """Updated targets"""

    timezone: str


class Media(TypedDict, total=False):
    url: Required[str]
    """Public URL of the media file"""

    type: Literal["image", "video", "gif", "document"]
    """Media type. Inferred from URL extension if omitted."""
