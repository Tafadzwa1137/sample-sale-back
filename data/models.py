
from dataclasses import dataclass


@dataclass
class Preference:
    id: int
    item_type: str
    description: str
    colour: str

@dataclass
class Recommendation:
    id: int
    item_type: str                      
    description: str
    colour: str