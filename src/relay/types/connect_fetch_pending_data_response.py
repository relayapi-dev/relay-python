# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectFetchPendingDataResponse", "UserProfile"]


class UserProfile(BaseModel):
    """Basic user profile from the platform"""

    id: str

    avatar_url: Optional[str] = None

    name: Optional[str] = None

    username: Optional[str] = None


class ConnectFetchPendingDataResponse(BaseModel):
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

    temp_token: str
    """Token to use for secondary selection"""

    user_profile: UserProfile
    """Basic user profile from the platform"""

    boards: Optional[List[Dict[str, Optional[object]]]] = None
    """Pinterest boards available"""

    locations: Optional[List[Dict[str, Optional[object]]]] = None
    """Google Business locations available"""

    organizations: Optional[List[Dict[str, Optional[object]]]] = None
    """LinkedIn organizations available"""

    pages: Optional[List[Dict[str, Optional[object]]]] = None
    """Facebook pages available"""

    profiles: Optional[List[Dict[str, Optional[object]]]] = None
    """Snapchat profiles available"""
