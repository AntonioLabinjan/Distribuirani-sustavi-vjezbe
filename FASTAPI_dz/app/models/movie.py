from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from .actor import Actor
from .writer import Writer


class Movie(BaseModel):
    Title: str
    Year: int = Field(..., gt=1900)
    Rated: str
    Runtime: int = Field(..., gt=0)
    Genre: str
    Language: str
    Country: str
    Actors: List[Actor]
    Plot: str
    Writer: List[Writer]

    imdbID: Optional[str] = None
    imdbRating: Optional[float] = Field(0.0, ge=0, le=10)
    imdbVotes: Optional[int] = Field(1, gt=0)
    Images: List[str] = Field(default_factory=list)
    type: Literal["movie", "series"] = "movie"
