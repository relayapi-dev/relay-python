# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["OrganizationListResponse", "Organization", "PersonalProfile"]


class Organization(BaseModel):
    name: str
    """Organization name"""

    urn: str
    """LinkedIn organization URN"""

    logo_url: Optional[str] = None
    """Organization logo URL"""

    vanity_name: Optional[str] = None
    """Organization vanity name"""


class PersonalProfile(BaseModel):
    """User's personal LinkedIn profile"""

    name: str

    urn: str


class OrganizationListResponse(BaseModel):
    organizations: List[Organization]

    personal_profile: Optional[PersonalProfile] = None
    """User's personal LinkedIn profile"""
