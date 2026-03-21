# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    enabled: bool
    """Enable or disable the webhook"""

    events: List[
        Literal[
            "post.published",
            "post.partial",
            "post.failed",
            "post.scheduled",
            "account.connected",
            "account.disconnected",
            "comment.received",
            "message.received",
        ]
    ]
    """Updated events"""

    url: str
    """Updated endpoint URL"""
