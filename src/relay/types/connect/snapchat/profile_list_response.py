# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ProfileListResponse", "Profile"]


class Profile(BaseModel):
    id: str
    """Snapchat profile ID"""

    display_name: str
    """Display name"""

    username: str
    """Snapchat username"""

    profile_image_url: Optional[str] = None
    """Profile image URL"""

    subscriber_count: Optional[int] = None
    """Number of subscribers"""


class ProfileListResponse(BaseModel):
    profiles: List[Profile]
