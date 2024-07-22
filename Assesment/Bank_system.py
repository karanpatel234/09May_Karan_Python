# bank_management.py

import json

class Banker:
    def _init_(self):
        self.customers = {}

    def add_customer(self):
        customer_id = input("Enter customer ID: ")
        name = input("Enter customer name: ")
        balance = float(input("Enter initial balance: "))
        self.customers[customer_id] = {"name": name, "balance": balance}
        print("Customer added successfully.")
        self.log_transaction("add_customer", customer_id)

    def view_customer(self):
        customer_id = input("Enter customer ID to view: ")
        if customer_id in self.customers:
            print(f"Customer ID: {customer_id}, Name: {self.customers[customer_id]['name']}, Balance: {self.customers[customer_id]['balance']}")
        else:
            print("Customer not found.")
        self.log_transaction("view_customer", customer_id)

    def search_customer(self):
        name = input("Enter customer name to search: ")
        found = False
        for customer_id, details in self.customers.items():
            if details["name"].lower() == name.lower():
                print(f"Customer ID: {customer_id}, Name: {details['name']}, Balance: {details['balance']}")
                found = True
        if not found:
            print("Customer not found.")
        self.log_transaction("search_customer", name)

    def view_all_customers(self):
        for customer_id, details in self.customers.items():
            print(f"Customer ID: {customer_id}, Name: {details['name']}, Balance: {details['balance']}")
        self.log_transaction("view_all_customers", "")

    def total_amounts(self):
        total = sum(details["balance"] for details in self.customers.values())
        print(f"Total amount in bank: {total}")
        self.log_transaction("total_amounts", "")

    def log_transaction(self, action, detail):
        with open("transaction_log.txt", "a") as log_file:
            log_file.write(f"Action: {action}, Detail: {detail}\n")


class Customer:
    def _init_(self, customers):
        self.customers = customers

    def deposit(self, customer_id):
        if customer_id in self.customers:
            amount = float(input("Enter amount to deposit: "))
            self.customers[customer_id]["balance"] += amount
            print("Amount deposited successfully.")
            self.log_transaction("deposit", customer_id, amount)
        else:
            print("Customer not found.")

    def withdraw(self, customer_id):
        if customer_id in self.customers:
            amount = float(input("Enter amount to withdraw: "))
            if self.customers[customer_id]["balance"] >= amount:
                self.customers[customer_id]["balance"] -= amount
                print("Amount withdrawn successfully.")
                self.log_transaction("withdraw", customer_id, amount)
            else:
                print("Insufficient balance.")
        else:
            print("Customer not found.")

    def view_balance(self, customer_id):
        if customer_id in self.customers:
            print(f"Current balance: {self.customers[customer_id]['balance']}")
            self.log_transaction("view_balance", customer_id)
        else:
            print("Customer not found.")

    def log_transaction(self, action, customer_id, amount=None):
        with open("transaction_log.txt", "a") as log_file:
            log_file.write(f"Action: {action}, Customer ID: {customer_id}, Amount: {amount}\n")


def display_menu():
    print("1. Banker")
    print("2. Customer")
    print("3. Exit")

def display_banker_menu():
    print("1. Add Customer")
    print("2. View Customer")
    print("3. Search Customer")
    print("4. View All Customers")
    print("5. Total Amounts")
    print("6. Back to Main Menu")

def display_customer_menu():
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. Back to Main Menu")

def main():
    banker = Banker()
    customers = banker.customers

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            while True:
                display_banker_menu()
                banker_choice = input("Enter your choice: ")
                if banker_choice == '1':
                    banker.add_customer()
                elif banker_choice == '2':
                    banker.view_customer()
                elif banker_choice == '3':
                    banker.search_customer()
                elif banker_choice == '4':
                    banker.view_all_customers()
                elif banker_choice == '5':
                    banker.total_amounts()
                elif banker_choice == '6':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '2':
            customer_id = input("Enter your customer ID: ")
            customer = Customer(customers)
            while True:
                display_customer_menu()
                customer_choice = input("Enter your choice: ")
                if customer_choice == '1':
                    customer.deposit(customer_id)
                elif customer_choice == '2':
                    customer.withdraw(customer_id)
                elif customer_choice == '3':
                    customer.view_balance(customer_id)
                elif customer_choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()