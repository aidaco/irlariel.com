# Aidan Courtney 2020, see incl. license for details.

from typing import Optional
import pydantic
from auth import AuthLevel

class User(pydantic.BaseModel):
    id: Optional[int] = None
    username: str
    pass_hash: str
    auth_level = AuthLevel.Basic