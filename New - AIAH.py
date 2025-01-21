class CashierProgram:
    def __init__(self):
        # Initialize bills and coins with starting quantities
        self.bills_and_coins = {
            "1000": 1,
            "500": 0,
            "200": 0,
            "100": 0,
            "50": 0,
            "20": 0,
            "10": 0,
            "5": 0,
            "1": 0,
            "0.25": 0, 
            "0.10": 0, 
            "0.05": 0, 
        }

    def customer_payment_and_change(self):
        print("\nCustomer Payment and Change:")

        total_payment = 0
        print("\nEnter the quantity of each bill/coin paid by the customer:")
        for denomination in self.bills_and_coins:
            while True:
                try:
                    quantity = int(input(f"{denomination} peso(s): "))
                    if quantity < 0:
                        print("Quantity cannot be negative. Skipping this denomination.")
                        continue
                    total_payment += float(denomination) * quantity
                    self.bills_and_coins[denomination] += quantity
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        print(f"\nTotal payment received: {total_payment:.2f} pesos")

        try:
            total_cost = float(input("Enter total amount to pay: "))
            change = total_payment - total_cost

            if change < 0:
                print("Error: Insufficient payment.")
                print("Requesting exact payment from the customer\n")
                return self.customer_payment_and_change()

            print(f"Total change to give: {change:.2f}")
            success = self.give_change(change)

            if not success:
                print("\nInsufficient change available.")
                print("Options:")
                print("1. Discard Transaction")
                print("2. Request Exact Payment")
                print("3. Cash Replenishment")
                while True:
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        self.discard_transaction(total_payment)
                        break
                    elif choice == "2":
                        print("Request exact payment\n")
                        return self.customer_payment_and_change()
                    elif choice == "3":
                        self.replenish_cash()
                        break
                    else:
                        print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

    def give_change(self, change):
        change_in_cents = int(change * 100)
        denominations = [
            (100000, "1000"), (50000, "500"), (20000, "200"),
            (10000, "100"), (5000, "50"), (2000, "20"),
            (1000, "10"), (500, "5"), (100, "1"),
            (25, "0.25"), (10, "0.10"), (5, "0.05")  
        ]
        
        print("\nGiving change:")
        insufficient_change = False

        for value_in_cents, denomination in denominations:
            if change_in_cents <= 0:
                break

            quantity_needed = change_in_cents // value_in_cents
            available_quantity = self.bills_and_coins[denomination]

            if quantity_needed > 0:
                quantity_to_give = min(quantity_needed, available_quantity)
                if quantity_to_give > 0:
                    self.bills_and_coins[denomination] -= quantity_to_give
                    change_in_cents -= quantity_to_give * value_in_cents
                    print(f"{denomination} peso(s): {quantity_to_give}")

        if change_in_cents > 0:
            shortfall = change_in_cents / 100
            print(f"Warning: Unable to provide full change. Shortfall: {shortfall:.2f} pesos.")
            return False

        print("Change given successfully.")
        return True

    def discard_transaction(self, total_payment):
        print("\nDiscarding transaction...")
        for denomination in sorted(self.bills_and_coins.keys(), key=float, reverse=True):
            value = float(denomination)
            if total_payment >= value:
                quantity_to_return = total_payment // value
                self.bills_and_coins[denomination] -= quantity_to_return
                total_payment %= value
                print(f"Returned {quantity_to_return} {denomination} peso(s) to inventory.")
        print("Transaction discarded. Inventory reverted.")

    def replenish_cash(self):
        print("\nReplenish Cash:")
        for denomination in self.bills_and_coins:
            while True:
                try:
                    quantity = int(input(f"Enter quantity to add for {denomination} peso(s): "))
                    if quantity < 0:
                        print("Quantity cannot be negative. Please try again.")
                        continue
                    self.bills_and_coins[denomination] += quantity
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        print("Cash replenishment completed successfully.")

    def display_quantities(self):
        print("\nCurrent quantities of bills and coins:")
        for denomination, quantity in self.bills_and_coins.items():
            print(f"{denomination} peso(s): {quantity}")

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Customer Payment and Change")
            print("2. Display Quantities")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.customer_payment_and_change()
            elif choice == "2":
                self.display_quantities()
            elif choice == "3":
                print("Exiting program")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the program
program = CashierProgram()
program.run()
