from pydantic import BaseModel
from typing import Optional

class Writer(BaseModel):
    name: str
    surname: Optional[str] = None

