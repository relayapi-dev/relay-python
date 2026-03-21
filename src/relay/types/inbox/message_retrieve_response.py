# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageRetrieveResponse", "Data", "DataAttachment"]


class DataAttachment(BaseModel):
    type: str
    """Attachment MIME type"""

    url: str
    """Attachment URL"""


class Data(BaseModel):
    id: str
    """Message ID"""

    created_at: datetime
    """Message timestamp"""

    sender: Literal["user", "participant"]
    """Message sender"""

    text: str
    """Message text"""

    attachments: Optional[List[DataAttachment]] = None
    """Message attachments"""


class MessageRetrieveResponse(BaseModel):
    data: List[Data]

    has_more: Optional[bool] = None

    next_cursor: Optional[str] = None
