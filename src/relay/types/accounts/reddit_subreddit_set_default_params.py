# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RedditSubredditSetDefaultParams"]


class RedditSubredditSetDefaultParams(TypedDict, total=False):
    subreddit: Required[str]
    """Subreddit name to set as default"""
