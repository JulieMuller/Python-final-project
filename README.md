# Python final project

You are required to create a console-based banking application in python that meets the following requirements outlined below. Where you find ambiguity in the requirements, you are expected to use your initiative and make a judgement call to complete the assignment.

## Logging in

1. An opening menu should ask if you are a Bank Employee or a Customer. 
2. To successfully login has a bank employee you must type in the pin 'A 1234'
3. To successfully login as a customer, you must enter your first name, last name, account number and pin.

### Bank Employee View

1. As a bank employee you can create and delete customers.
2. Each new customer gets a savings account and a current account.
3. You can only delete customers who have zero balances.
4. You can create transactions (lodge, deposit) for cach customer. You should be able to add and withdraw for a specified account.
5. To create a customer account you need first name, last name and email. 6. You should be able to show a complete list of customers including their balances in savings and current account. 7. There should be a menu item allowing you to list customers, their account numbers.

### Customer View

1. To login, a customer must enter their name, account code AND a pin number for their account
2. A customer can retrieve the transaction history for their specified account.
3. They can add and subtract money to either their savings account or current account.
4. They cannot have negative balances

### Creating Accounts

1. Your application should create a file called customers.txt which stores a list of customer accounts. Each account should be stored on a single line; it is up to you to decide the format. This file should be created when the program runs for the first time.

2. The system should create accounts based on the following rules:
The filename will be called xx-nn-yy-zz where xx is the initials of the customer, an is the length of the total name (first name and last name, yy is the alphabetical position of the first initial and zz is the alphabetical position of the second initial (see table below)- together they make up the pin number