# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TelegramPollConnectionStatusParams"]


class TelegramPollConnectionStatusParams(TypedDict, total=False):
    code: Required[str]
    """The 6-character access code to check"""
