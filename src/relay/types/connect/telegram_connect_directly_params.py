# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TelegramConnectDirectlyParams"]


class TelegramConnectDirectlyParams(TypedDict, total=False):
    chat_id: Required[str]
    """Telegram chat or channel ID"""
