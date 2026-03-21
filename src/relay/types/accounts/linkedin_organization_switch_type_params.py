# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkedinOrganizationSwitchTypeParams"]


class LinkedinOrganizationSwitchTypeParams(TypedDict, total=False):
    account_type: Required[Literal["personal", "organization"]]
    """Account type to switch to"""

    organization_id: Required[str]
    """LinkedIn organization ID"""
