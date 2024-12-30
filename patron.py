from dataclasses import dataclass

from PIL.ImageQt import ImageQt
from PyQt6.QtGui import QMovie

from order import Order


@dataclass
class Patron:
    id: int
    name: str
    orders: list[Order]
    balance: float
    photo: ImageQt
    movie: QMovie = None

    @property
    def active_order(self) -> Order | None:
        for order in self.orders:
            if not order.settled:
                return order

    @active_order.setter
    def active_order(self, updated_order):
        for order in self.orders:
            if not order.settled:
                order.__dict__.update(updated_order.__dict__)
                break

    @property
    def settled_orders(self) -> list[Order]:
        return [order for order in self.orders if order.settled]
