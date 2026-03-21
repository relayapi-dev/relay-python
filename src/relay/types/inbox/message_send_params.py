# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MessageSendParams", "Attachment"]


class MessageSendParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID to send from"""

    text: Required[str]
    """Message text"""

    attachments: Iterable[Attachment]
    """Attachments"""

    message_tag: str
    """Message tag (e.g. for Facebook outside 24h window)"""

    reply_to: str
    """Message ID to reply to"""


class Attachment(TypedDict, total=False):
    type: Required[str]
    """Attachment MIME type"""

    url: Required[str]
    """Attachment URL"""
