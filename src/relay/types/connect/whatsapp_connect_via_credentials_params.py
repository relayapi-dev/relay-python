# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WhatsappConnectViaCredentialsParams"]


class WhatsappConnectViaCredentialsParams(TypedDict, total=False):
    access_token: Required[str]
    """WhatsApp Business API access token"""

    phone_number_id: Required[str]
    """WhatsApp phone number ID"""

    waba_id: Required[str]
    """WhatsApp Business Account ID"""
