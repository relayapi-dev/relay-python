# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectCompleteOAuthCallbackParams"]


class ConnectCompleteOAuthCallbackParams(TypedDict, total=False):
    code: Required[str]
    """OAuth authorization code"""

    redirect_url: str
    """Redirect URL used during the OAuth flow (must match)"""
