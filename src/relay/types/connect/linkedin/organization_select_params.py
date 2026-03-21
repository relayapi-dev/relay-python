# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OrganizationSelectParams"]


class OrganizationSelectParams(TypedDict, total=False):
    account_type: Required[Literal["personal", "organization"]]
    """Whether to connect as a personal profile or organization"""

    connect_token: Required[str]
    """Token from pending data or OAuth flow"""

    organization_urn: str
    """LinkedIn organization URN (required if account_type is organization)"""
