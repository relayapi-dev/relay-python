# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = [
    "ValidateCheckPostLengthResponse",
    "Platforms",
    "PlatformsBluesky",
    "PlatformsDiscord",
    "PlatformsFacebook",
    "PlatformsGooglebusiness",
    "PlatformsInstagram",
    "PlatformsLinkedin",
    "PlatformsMastodon",
    "PlatformsPinterest",
    "PlatformsReddit",
    "PlatformsSMS",
    "PlatformsSnapchat",
    "PlatformsTelegram",
    "PlatformsThreads",
    "PlatformsTiktok",
    "PlatformsTwitter",
    "PlatformsWhatsapp",
    "PlatformsYoutube",
]


class PlatformsBluesky(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsDiscord(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsFacebook(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsGooglebusiness(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsInstagram(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsLinkedin(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsMastodon(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsPinterest(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsReddit(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsSMS(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsSnapchat(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsTelegram(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsThreads(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsTiktok(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsTwitter(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsWhatsapp(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class PlatformsYoutube(BaseModel):
    count: float
    """Character count for this platform"""

    limit: float
    """Character limit for this platform"""

    within_limit: bool
    """Whether content is within limit"""


class Platforms(BaseModel):
    """Character count per platform"""

    bluesky: Optional[PlatformsBluesky] = None

    discord: Optional[PlatformsDiscord] = None

    facebook: Optional[PlatformsFacebook] = None

    googlebusiness: Optional[PlatformsGooglebusiness] = None

    instagram: Optional[PlatformsInstagram] = None

    linkedin: Optional[PlatformsLinkedin] = None

    mastodon: Optional[PlatformsMastodon] = None

    pinterest: Optional[PlatformsPinterest] = None

    reddit: Optional[PlatformsReddit] = None

    sms: Optional[PlatformsSMS] = None

    snapchat: Optional[PlatformsSnapchat] = None

    telegram: Optional[PlatformsTelegram] = None

    threads: Optional[PlatformsThreads] = None

    tiktok: Optional[PlatformsTiktok] = None

    twitter: Optional[PlatformsTwitter] = None

    whatsapp: Optional[PlatformsWhatsapp] = None

    youtube: Optional[PlatformsYoutube] = None


class ValidateCheckPostLengthResponse(BaseModel):
    platforms: Platforms
    """Character count per platform"""
