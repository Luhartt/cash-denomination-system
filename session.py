class Session:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Session, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "transactions"):
            self.transactions = []
        if not hasattr(self, "coins_and_bills"):
            self.coins_and_bills = {       
                "1000": 100,
                "500": 100,
                "200": 100,
                "100": 100,
                "50": 100,
                "20": 100,
                "10": 100,
                "5": 100,
                "1": 100,
                "0.25": 100, 
                "0.10": 100, 
                "0.05": 100, 
                }
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

    def get_coins_and_bills(self):
        return self.coins_and_bills
    
    def add_coins_and_bills(self, type, to_add):
        self.coins_and_bills[f"{type}"] += int(to_add)