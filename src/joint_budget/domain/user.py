from dataclasses import dataclass, field
from typing import Set, Iterable
from .id_generator import get_next_unique_id
from .transfer import Transfer


@dataclass
class User:
    name: str
    transfers: Set[Transfer] = field(default_factory=list)
    budget_ids: Set[str] = field(default_factory=list)
    id: str = field(default_factory=get_next_unique_id)

    def add_transfers(self, transfers: Set[Transfer]):
        self.transfers.update(transfers)

    def add_transfer(self, transfer: Transfer):
        self.transfers.add(transfer)
