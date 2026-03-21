# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TemplateCreateParams", "Component", "ComponentButton"]


class TemplateCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """WhatsApp account ID"""

    category: Required[Literal["MARKETING", "UTILITY", "AUTHENTICATION"]]
    """Template category"""

    components: Required[Iterable[Component]]
    """Template components"""

    language: Required[str]
    """Template language code"""

    name: Required[str]
    """Template name"""


class ComponentButton(TypedDict, total=False):
    text: Required[str]
    """Button text"""

    type: Required[str]
    """Button type"""

    phone_number: str

    url: str


class Component(TypedDict, total=False):
    type: Required[Literal["HEADER", "BODY", "FOOTER", "BUTTONS"]]
    """Component type"""

    buttons: Iterable[ComponentButton]

    format: str
    """Header format (TEXT, IMAGE, etc.)"""

    text: str
    """Component text"""
