import random


class Transaction:

    def __init__(self, operation):
        self._operation = operation
        self._client = random.randint(1000, 1500)
        self._product = random.randint(100, 150)
        self._quantity = random.randint(10, 15)

    def get_info(self):
        return {"Operation": self._operation,
                "Client": self._client,
                "Product": self._product,
                "Quantity": self._quantity}
