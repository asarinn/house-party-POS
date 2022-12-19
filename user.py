from drink import Drink


class User:
    def __init__(self, name: str):
        self._name: str = name
        self._total: float = 0
        self._paid: float = 0
        self._balance: float = 0
        self._drinks = []

    @property
    def name(self):
        return

    @name.setter
    def name(self, value):
        pass

    @property
    def total(self):
        return

    @total.setter
    def total(self, value):
        pass

    @property
    def paid(self):
        return

    @paid.setter
    def paid(self, value):
        pass

    @property
    def balance(self):
        return

    @balance.setter
    def balance(self, value):
        pass

    @property
    def drinks(self):
        return

    def add_drink(self, drink: Drink, quantity: int):
        # Add to list

        # Recalculate Balance
        pass