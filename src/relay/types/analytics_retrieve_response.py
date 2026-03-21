# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AnalyticsRetrieveResponse", "Data", "Overview"]


class Data(BaseModel):
    platform: Literal[
        "twitter",
        "instagram",
        "facebook",
        "linkedin",
        "tiktok",
        "youtube",
        "pinterest",
        "reddit",
        "bluesky",
        "threads",
        "telegram",
        "snapchat",
        "googlebusiness",
        "whatsapp",
        "mastodon",
        "discord",
        "sms",
    ]

    post_id: str
    """Post ID"""

    published_at: datetime
    """Published timestamp"""

    clicks: Optional[float] = None
    """Total clicks"""

    comments: Optional[float] = None
    """Total comments"""

    impressions: Optional[float] = None
    """Total impressions"""

    likes: Optional[float] = None
    """Total likes"""

    reach: Optional[float] = None
    """Total reach"""

    saves: Optional[float] = None
    """Total saves"""

    shares: Optional[float] = None
    """Total shares"""

    views: Optional[float] = None
    """Total views"""


class Overview(BaseModel):
    total_clicks: float
    """Total clicks across posts"""

    total_comments: float
    """Total comments across posts"""

    total_impressions: float
    """Total impressions across posts"""

    total_likes: float
    """Total likes across posts"""

    total_posts: float
    """Total number of posts"""

    total_shares: float
    """Total shares across posts"""

    total_views: float
    """Total views across posts"""


class AnalyticsRetrieveResponse(BaseModel):
    data: List[Data]

    overview: Optional[Overview] = None
