# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WhatsappBulkSendParams", "Recipient", "Template", "TemplateComponent"]


class WhatsappBulkSendParams(TypedDict, total=False):
    account_id: Required[str]
    """WhatsApp account ID"""

    recipients: Required[Iterable[Recipient]]
    """Recipients"""

    template: Required[Template]


class Recipient(TypedDict, total=False):
    phone: Required[str]
    """Phone number in E.164 format"""

    variables: Dict[str, str]
    """Template variable substitutions"""


class TemplateComponent(TypedDict, total=False):
    type: Required[Literal["header", "body", "button"]]
    """Component type"""

    parameters: Iterable[Dict[str, Optional[object]]]
    """Component parameters"""


class Template(TypedDict, total=False):
    language: Required[str]
    """Template language code"""

    name: Required[str]
    """Template name"""

    components: Iterable[TemplateComponent]
    """Template components"""
