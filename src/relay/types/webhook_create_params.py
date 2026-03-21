# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    events: Required[
        List[
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
    ]
    """Events to subscribe to"""

    url: Required[str]
    """Webhook endpoint URL"""
