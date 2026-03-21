# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TemplateCreateResponse", "Component", "ComponentButton"]


class ComponentButton(BaseModel):
    text: str
    """Button text"""

    type: str
    """Button type"""

    phone_number: Optional[str] = None

    url: Optional[str] = None


class Component(BaseModel):
    type: Literal["HEADER", "BODY", "FOOTER", "BUTTONS"]
    """Component type"""

    buttons: Optional[List[ComponentButton]] = None

    format: Optional[str] = None
    """Header format (TEXT, IMAGE, etc.)"""

    text: Optional[str] = None
    """Component text"""


class TemplateCreateResponse(BaseModel):
    category: Literal["MARKETING", "UTILITY", "AUTHENTICATION"]
    """Template category"""

    components: List[Component]

    language: str
    """Template language code"""

    name: str
    """Template name"""

    status: Literal["APPROVED", "PENDING", "REJECTED"]
    """Approval status"""
