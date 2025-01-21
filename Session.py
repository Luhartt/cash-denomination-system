class Session:
    _instance = None
    
    def __init__(self):
        # Initialize instance variables
        self.payment_denomination = {}
        self.total_bill = 0
        self.total_payment = 0
        self.total_change = 0
    
    # Singleton class to be used as a single instance throughout the whole session
    def __new__(cls):  
        if cls._instance is None:  
            cls._instance = super().__new__(cls)
            cls._instance.__init__()
        return cls._instance
    
    def reset_vars(self):
        """Reset all instance variables to their initial state"""
        self.payment_denomination = {}
        self.total_bill = 0
        self.total_payment = 0
        self.total_change = 0
        
    def get_total_bill(self):
        return self.total_bill
        
    def get_total_payment(self):
        return self.total_payment
        
    def get_payment_denomination(self):
        return self.payment_denomination
        
    def get_total_change(self):
        return self.total_change
    
    def set_total_bill(self, value):
        self.total_bill = value
        
    def set_total_payment(self, value):
        self.total_payment = value
        
    def set_payment_denomination(self, value):
        self.payment_denomination = value
        
    def set_total_change(self, value):
        self.total_change = value