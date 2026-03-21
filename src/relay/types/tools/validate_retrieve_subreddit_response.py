# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ValidateRetrieveSubredditResponse", "PostTypes"]


class PostTypes(BaseModel):
    """Allowed post types"""

    image: bool
    """Allows image posts"""

    link: bool
    """Allows link posts"""

    self: bool
    """Allows text posts"""


class ValidateRetrieveSubredditResponse(BaseModel):
    exists: bool
    """Whether the subreddit exists"""

    name: Optional[str] = None
    """Canonical subreddit name"""

    nsfw: Optional[bool] = None
    """Whether NSFW"""

    post_types: Optional[PostTypes] = None
    """Allowed post types"""

    subscribers: Optional[float] = None
    """Subscriber count"""

    title: Optional[str] = None
    """Subreddit title"""
