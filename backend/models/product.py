# Aidan Courtney 2020, see incl. license for details.

from typing import Optional, Dict
from datetime import datetime
import pydantic

class Product(pydantic.BaseModel):
    id: Optional[int] = None
    title: str = "Untitled"
    description: str = "No description found."
    list_date: Optional[datetime] = None
    imgs: Optional[dict[str, str]] = None
