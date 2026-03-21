# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["RedditGetFeedResponse", "Data"]


class Data(BaseModel):
    id: str
    """Reddit post ID"""

    author: str
    """Post author"""

    created_utc: float
    """Created timestamp (Unix)"""

    is_self: bool
    """Whether it's a self post"""

    nsfw: bool
    """Whether NSFW"""

    num_comments: float
    """Comment count"""

    score: float
    """Post score"""

    subreddit: str
    """Subreddit name"""

    title: str
    """Post title"""

    url: str
    """Post URL"""

    selftext: Optional[str] = None
    """Self text"""

    thumbnail: Optional[str] = None
    """Thumbnail URL"""


class RedditGetFeedResponse(BaseModel):
    data: List[Data]

    has_more: bool

    next_cursor: Optional[str] = None
