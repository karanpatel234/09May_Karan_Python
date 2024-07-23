# Simple Bank Management System

customers = {}

def add_customer():
    customer_id = input("Enter customer ID: ")
    name = input("Enter customer name: ")
    balance = float(input("Enter initial balance: "))
    customers[customer_id] = {"name": name, "balance": balance}
    print("Customer added successfully.")
    log_transaction("add_customer", customer_id)

def view_customer():
    customer_id = input("Enter customer ID to view: ")
    if customer_id in customers:
        print(f"Customer ID: {customer_id}, Name: {customers[customer_id]['name']}, Balance: {customers[customer_id]['balance']}")
    else:
        print("Customer not found.")
    log_transaction("view_customer", customer_id)

def search_customer():
    name = input("Enter customer name to search: ")
    found = False
    for customer_id, details in customers.items():
        if details["name"].lower() == name.lower():
            print(f"Customer ID: {customer_id}, Name: {details['name']}, Balance: {details['balance']}")
            found = True
    if not found:
        print("Customer not found.")
    log_transaction("search_customer", name)

def view_all_customers():
    for customer_id, details in customers.items():
        print(f"Customer ID: {customer_id}, Name: {details['name']}, Balance: {details['balance']}")
    log_transaction("view_all_customers", "")

def total_amounts():
    total = sum(details["balance"] for details in customers.values())
    print(f"Total amount in bank: {total}")
    log_transaction("total_amounts", "")

def deposit():
    customer_id = input("Enter your customer ID: ")
    if customer_id in customers:
        amount = float(input("Enter amount to deposit: "))
        customers[customer_id]["balance"] += amount
        print("Amount deposited successfully.")
        log_transaction("deposit", customer_id, amount)
    else:
        print("Customer not found.")

def withdraw():
    customer_id = input("Enter your customer ID: ")
    if customer_id in customers:
        amount = float(input("Enter amount to withdraw: "))
        if customers[customer_id]["balance"] >= amount:
            customers[customer_id]["balance"] -= amount
            print("Amount withdrawn successfully.")
            log_transaction("withdraw", customer_id, amount)
        else:
            print("Insufficient balance.")
    else:
        print("Customer not found.")

def view_balance():
    customer_id = input("Enter your customer ID: ")
    if customer_id in customers:
        print(f"Current balance: {customers[customer_id]['balance']}")
        log_transaction("view_balance", customer_id)
    else:
        print("Customer not found.")

def log_transaction(action, customer_id, amount=None):
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

# Main program execution

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        while True:
            display_banker_menu()
            banker_choice = input("Enter your choice: ")
            if banker_choice == '1':
                add_customer()
            elif banker_choice == '2':
                view_customer()
            elif banker_choice == '3':
                search_customer()
            elif banker_choice == '4':
                view_all_customers()
            elif banker_choice == '5':
                total_amounts()
            elif banker_choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")
    elif choice == '2':
        customer_id = input("Enter your customer ID: ")
        while True:
            display_customer_menu()
            customer_choice = input("Enter your choice: ")
            if customer_choice == '1':
                deposit()
            elif customer_choice == '2':
                withdraw()
            elif customer_choice == '3':
                view_balance()
            elif customer_choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")