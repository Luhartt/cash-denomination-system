class Transactions:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Transactions, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "transactions"):
            self.transactions = []

    def get_transactions(self):
        return self.transactions

    def add_transaction(self, time, amount):
        """
        Add a new transaction to the transactions set.

        :param time: A string representing the time of the transaction (e.g., "15:30").
        :param amount: A string representing the amount (e.g., "+500" or "-200").
        """
        if not isinstance(time, str) or not isinstance(amount, str):
            raise ValueError("Time and amount must be strings.")

        self.transactions.append((time, amount))

