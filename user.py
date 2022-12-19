from drink import Drink


class User:
    def __init__(self, name: str):
        self.name: str = name  # Used to match against orders in the database
        self._total: float = 0
        self._paid: float = 0
        self._balance: float = 0
        self._drinks: list[tuple[str, int]] = []
        self.current_order_number = 0

    # Retrieve current total from all open orders in database
    @property
    def total(self):
        return

    # Returns a list of drinks and quantities from all open orders
    @property
    def drinks(self):
        return

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
