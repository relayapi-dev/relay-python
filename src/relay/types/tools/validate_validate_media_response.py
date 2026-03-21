# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = [
    "ValidateValidateMediaResponse",
    "PlatformLimits",
    "PlatformLimitsBluesky",
    "PlatformLimitsDiscord",
    "PlatformLimitsFacebook",
    "PlatformLimitsGooglebusiness",
    "PlatformLimitsInstagram",
    "PlatformLimitsLinkedin",
    "PlatformLimitsMastodon",
    "PlatformLimitsPinterest",
    "PlatformLimitsReddit",
    "PlatformLimitsSMS",
    "PlatformLimitsSnapchat",
    "PlatformLimitsTelegram",
    "PlatformLimitsThreads",
    "PlatformLimitsTiktok",
    "PlatformLimitsTwitter",
    "PlatformLimitsWhatsapp",
    "PlatformLimitsYoutube",
]


class PlatformLimitsBluesky(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsDiscord(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsFacebook(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsGooglebusiness(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsInstagram(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsLinkedin(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsMastodon(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsPinterest(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsReddit(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsSMS(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsSnapchat(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsTelegram(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsThreads(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsTiktok(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsTwitter(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsWhatsapp(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimitsYoutube(BaseModel):
    max_size: float
    """Maximum file size in bytes"""

    within_limit: bool
    """Whether file size is within limit"""


class PlatformLimits(BaseModel):
    """Per-platform size limits"""

    bluesky: Optional[PlatformLimitsBluesky] = None

    discord: Optional[PlatformLimitsDiscord] = None

    facebook: Optional[PlatformLimitsFacebook] = None

    googlebusiness: Optional[PlatformLimitsGooglebusiness] = None

    instagram: Optional[PlatformLimitsInstagram] = None

    linkedin: Optional[PlatformLimitsLinkedin] = None

    mastodon: Optional[PlatformLimitsMastodon] = None

    pinterest: Optional[PlatformLimitsPinterest] = None

    reddit: Optional[PlatformLimitsReddit] = None

    sms: Optional[PlatformLimitsSMS] = None

    snapchat: Optional[PlatformLimitsSnapchat] = None

    telegram: Optional[PlatformLimitsTelegram] = None

    threads: Optional[PlatformLimitsThreads] = None

    tiktok: Optional[PlatformLimitsTiktok] = None

    twitter: Optional[PlatformLimitsTwitter] = None

    whatsapp: Optional[PlatformLimitsWhatsapp] = None

    youtube: Optional[PlatformLimitsYoutube] = None


class ValidateValidateMediaResponse(BaseModel):
    accessible: bool
    """Whether the URL is accessible"""

    platform_limits: PlatformLimits
    """Per-platform size limits"""

    content_type: Optional[str] = None
    """MIME type"""

    size: Optional[float] = None
    """File size in bytes"""
