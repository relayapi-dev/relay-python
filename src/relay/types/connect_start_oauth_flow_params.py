# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConnectStartOAuthFlowParams"]


class ConnectStartOAuthFlowParams(TypedDict, total=False):
    headless: str
    """Set to "true" for headless mode (returns data instead of redirecting)"""

    redirect_url: str
    """URL to redirect after OAuth completes"""
