import csv
from datetime import datetime
import os


class TransactionHistory:
    def __init__(self, filename="transactions.csv"):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Transaction_Number', 'Date', 'Amount', 'Balance'])

    def add_transaction(self, amount):
        current_balance = 0
        transaction_number = 1

        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if row:
                        transaction_number = int(row[0]) + 1
                        current_balance = float(row[3])

        new_balance = current_balance + amount

        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                transaction_number,
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                amount,
                new_balance
            ])

    def view_history(self):
        transactions = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if row:
                        transactions.append({
                            'transaction_number': int(row[0]),
                            'date': row[1],
                            'amount': float(row[2]),
                            'balance': float(row[3])
                        })
        return transactions


def main():
    history = TransactionHistory()

    while True:
        print("\n=== Transaction Management System ===")
        print("1. Add Transaction")
        print("2. View History")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            try:
                amount = float(input("\nEnter amount (positive for deposit, negative for withdrawal): "))
                history.add_transaction(amount)
                print(f"Transaction of ${abs(amount):.2f} {'added' if amount > 0 else 'subtracted'} successfully!")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == '2':
            transactions = history.view_history()
            if not transactions:
                print("\nNo transactions found.")
            else:
                print("\n=== Transaction History ===")
                print("No.  |  Date                  |  Amount     |  Balance")
                print("-" * 55)
                for t in transactions:
                    print(
                        f"{t['transaction_number']:<5}|  {t['date']:<21}|  ${t['amount']:>9.2f}|  ${t['balance']:>8.2f}")

        elif choice == '3':
            print("\nThank you for using the Transaction Management System!")
            break

        else:
            print("\nInvalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()