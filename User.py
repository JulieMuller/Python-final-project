import json

class User:

    def __init__(self, first_name, last_name, email, account_number, password, savings_account = 0.0, current_account = 0.0):
        self.status = "User"  # Default status is Active
        self.savings_account = float(savings_account)  # Default savings account balance is 0.0
        self.current_account = float(current_account)  # Default current account balance is 0.0
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        self.email = email
        self.account_number = str(account_number)
        self.password = str(password)

    def Copy(self, user):
        self.status = user.status
        self.savings_account = user.savings_account
        self.current_account = user.current_account
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.email = user.email
        self.account_number = user.account_number
        self.password = user.password

    def user_update(self, users_list):
        self.save(users_list)
        User.load_users_from_file()
    
    def load_users_from_file(filename="users.txt"):
        users_list = []
        try:
            file = open(filename, 'r')
            for line in file.readlines():
                customer_data = line[:-1].split(" ")
                users_list.append(User(customer_data[0], 
                                       customer_data[1], 
                                       customer_data[2],
                                       customer_data[3],
                                       customer_data[4],
                                       customer_data[5],
                                       customer_data[6]))
        except FileNotFoundError:
            # Handle the case where the file does not exist
            pass
        return users_list

    def already_exist(self, user_list): #if the user exists already returns true
        for users in user_list:
            if (self.first_name == users.first_name or
                    self.last_name.lower() == users.last_name or
                    self.email == users.email or
                    self.account_number == users.account_number) :
                return True
            else: return False
            
    def login_form_validation(self, user_list): #if the user exists returns true
        for i in range(len(user_list)):
            if (self.first_name == user_list[i].first_name and
                    self.last_name == user_list[i].last_name and
                    self.account_number == user_list[i].account_number and
                    self.password == user_list[i].password):
                return (True,i)
            else:
                pass
        return (False, False)

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Savings Account Balance: ${self.savings_account}")
        print(f"Current Account Balance: ${self.current_account}")
        print(f"Account Number: {self.account_number}")
        print(f"Mdp: {self.password}")


    def deposit(self, account_type, amount):
        if account_type.lower() == "savings":
            self.savings_account += float(amount)
        elif account_type.lower() == "current":
            self.current_account += float(amount)
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

    def save(self, users_list, filename="users.txt"):
        file = open(filename, 'w')
        for users in users_list:
            customer_data = (str(users.first_name) + " " + 
                             str(users.last_name) + " " + 
                             str(users.email) + " " + 
                             str(users.account_number) + " " + 
                             str(users.password) + " " + 
                             str(users.savings_account) + " " +  
                             str(users.current_account) + " " + 
                             str(users.status))
            file.writelines(customer_data + '\n')