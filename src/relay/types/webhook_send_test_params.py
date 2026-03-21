# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WebhookSendTestParams"]


class WebhookSendTestParams(TypedDict, total=False):
    webhook_id: Required[str]
    """ID of the webhook to test"""
