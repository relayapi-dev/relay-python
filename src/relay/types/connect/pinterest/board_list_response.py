# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["BoardListResponse", "Board"]


class Board(BaseModel):
    id: str
    """Pinterest board ID"""

    name: str
    """Board name"""

    description: Optional[str] = None
    """Board description"""

    pin_count: Optional[int] = None
    """Number of pins on the board"""


class BoardListResponse(BaseModel):
    boards: List[Board]
