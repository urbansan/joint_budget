from dataclasses import dataclass, field
from typing import List
from .id_generator import get_next_unique_id
from .record import Record


@dataclass
class User:
    name: str
    record: List[Record]
    budget_ids: List[str] = field(default_factory=list)
    id: str = field(default_factory=get_next_unique_id)
