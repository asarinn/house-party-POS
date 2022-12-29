from dataclasses import dataclass
from datetime import datetime


@dataclass
class OrderItem:
    id: int
    drink: str
    price: float
    quantity: int

    @property
    def total(self) -> float:
        return self.price * self.quantity


@dataclass
class Order:
    id: int
    order_items: list[OrderItem]
    total: float
    patron: str
    settled: bool
    created: datetime
