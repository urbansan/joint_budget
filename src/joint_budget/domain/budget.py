from dataclasses import dataclass, field
from .id_generator import get_next_unique_id


@dataclass
class Budget:
    user_ids: list = field(default_factory=list)
    id: str = field(default_factory=get_next_unique_id)

    # TODO: budget strategies
