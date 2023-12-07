import json

class User:
    def __init__(self, first_name, last_name, email, account_numbers, pin_number):
        self.status = "Active"  # Default status is Active
        self.savings_account = 0.0  # Default savings account balance is 0.0
        self.current_account = 0.0  # Default current account balance is 0.0
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.account_numbers = account_numbers
        self.pin_number = pin_number

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Savings Account Balance: ${self.savings_account}")
        print(f"Current Account Balance: ${self.current_account}")
        print(f"Account Numbers: {', '.join(map(str, self.account_numbers))}")
        # For security reasons, we don't display the PIN number in the information.

    def deposit(self, account_type, amount):
        if account_type.lower() == "savings":
            self.savings_account += amount
        elif account_type.lower() == "current":
            self.current_account += amount
        else:
            print("Invalid account type. Use 'savings' or 'current'.")

    def withdraw(self, account_type, amount):
        if account_type.lower() == "savings":
            if amount <= self.savings_account:
                self.savings_account -= amount
            else:
                print("Insufficient funds in the savings account.")
        elif account_type.lower() == "current":
            if amount <= self.current_account:
                self.current_account -= amount
            else:
                print("Insufficient funds in the current account.")
        else:
            print("Invalid account type. Use 'savings' or 'current'.")

    def save(self, filename="customers.txt"):
        customer_data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "account_numbers": self.account_numbers,
            "pin_number": self.pin_number,
            "savings_account": self.savings_account,
            "current_account": self.current_account,
            "status": self.status
        }

        with open(filename, 'a') as file:
            file.write(json.dumps(customer_data) + '\n')