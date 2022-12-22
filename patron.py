from PyQt6.QtWidgets import QPushButton

from drink import Drink


class Patron:
    def __init__(self, name: str):
        self.name: str = name  # Used to match against orders in the database
        self.button: QPushButton | None = None  # holds its own gui button to make gui modifications easier
        self._total: float = 0
        self._drinks: list[tuple[object, int]] = []
        self.current_order_number = 0

        # TODO(from Mike): remove this once database connections are made
        cup_of_spit = Drink('cup of spit', 1.25)
        cold_fries = Drink('cold fries', .33)
        self._drinks = [[cup_of_spit, 5], (cold_fries, 1)]

    # Retrieve current total from all open orders in database
    @property
    def total(self):
        # TODO(from Mike): Update from database here
        return self._total

    # Returns a list of drinks and quantities from all open orders
    @property
    def drinks(self):
        # TODO(from Mike): Update from database here
        return self._drinks

    def add_drink(self, drink: Drink, quantity: int):
        # Check to see if any orders are open, open a new one and associate order number if needed

        # Add this drink to database

        pass

    def remove_drink(self, drink: Drink, quantity: int):
        # Check all open user orders, throw warning if drink does not exist in any open customer orders

        # Remove drink in quantity from database

        pass

    def settle_up(self):
        # Settle up all open orders on database
        pass
