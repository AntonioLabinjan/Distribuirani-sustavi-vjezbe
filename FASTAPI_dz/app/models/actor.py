# actor.py
from pydantic import BaseModel
from typing import Optional

class Actor(BaseModel):
    name: str
    surname: Optional[str] = None
