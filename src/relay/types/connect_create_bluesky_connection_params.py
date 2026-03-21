# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectCreateBlueskyConnectionParams"]


class ConnectCreateBlueskyConnectionParams(TypedDict, total=False):
    app_password: Required[str]
    """Bluesky app password"""

    handle: Required[str]
    """Bluesky handle (e.g. user.bsky.social)"""
