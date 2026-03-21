# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AnalyticsGetContentDecayResponse", "Data"]


class Data(BaseModel):
    cumulative_engagement: float
    """Cumulative engagement"""

    cumulative_impressions: float
    """Cumulative impressions"""

    day: float
    """Days since publication"""

    engagement: float
    """Engagement on this day"""

    impressions: float
    """Impressions on this day"""


class AnalyticsGetContentDecayResponse(BaseModel):
    data: List[Data]

    half_life_days: Optional[float] = None
    """Days until engagement halved"""

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
