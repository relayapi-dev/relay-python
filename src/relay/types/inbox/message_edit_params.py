# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MessageEditParams"]


class MessageEditParams(TypedDict, total=False):
    conversation_id: Required[str]
    """Conversation ID"""

    text: Required[str]
    """Updated message text"""
