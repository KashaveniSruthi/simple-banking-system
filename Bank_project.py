# Dictionary to store customer details {name: (pin, balance)}
customers = {
    "Shruthi": ("2199", 91010),
    "Jyothi": ("9144", 8110),
    "Samsritha": ("9121", 57310),
    "Shirisha": ("9703", 18310),
    "Harsha": ("8374", 21710),
    "Varsha": ("1234", 63020),
}

# Dictionary to store mini-statements {name: [transactions]}
transactions = {name: [] for name in customers}

# Function to handle deposits & withdrawals
def transaction(name, pin, amount, operation):
    if name in customers and customers[name][0] == pin:
        balance = customers[name][1]
        if operation == "withdraw":
            if amount > balance:
                print(" Insufficient funds!")
            else:
                customers[name] = (pin, balance - amount)
                transactions[name].append(f"Withdrawn: -{amount} | Balance: {customers[name][1]}")
                print(f"Withdrawn {amount}. New Balance: {customers[name][1]}")
        elif operation == "deposit":
            customers[name] = (pin, balance + amount)
            transactions[name].append(f"Deposited: +{amount} | Balance: {customers[name][1]}")
            print(f" Deposited {amount}. New Balance: {customers[name][1]}")
    else:
        print(" Invalid name or PIN!")

# Function to delete an account
def delete_account():
    name = input("Enter name: ").strip()
    pin = input("Enter PIN: ").strip()
    if name in customers and customers[name][0] == pin:
        del customers[name]
        del transactions[name]
        print(" Account deleted successfully!")
    else:
        print(" Account not found or incorrect PIN!")

# Function to show mini-statement
def mini_statement():
    name = input("Enter name: ").strip()
    pin = input("Enter PIN: ").strip()
    if name in customers and customers[name][0] == pin:
        print(f"\n Mini-Statement for {name}:")
        for record in transactions[name]:
            print(f" {record}")
        if not transactions[name]:
            print(" No transactions yet!")
    else:
        print(" Invalid name or PIN!")

# Main menu loop
while True:
    print("\n********* Welcome to State Bank *********")
    print("1. Open a New Account")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. View Customers & Balances")
    print("5. View Mini-Statement")
    print("6. Delete Account")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":  # Open a new account
        name = input("Enter full name: ").strip()
        if name in customers:
            print(" Account already exists!")
            continue
        pin = input("Set a 4-digit PIN: ").strip()
        if not pin.isdigit() or len(pin) != 4:
            print(" Invalid PIN! Must be 4 digits.")
            continue
        deposit = int(input("Enter initial deposit: "))
        customers[name] = (pin, deposit)
        transactions[name] = [f"Account Opened | Initial Deposit: {deposit}"]
        print(" Account created successfully!")

    elif choice == "2":  # Withdraw money
        name = input("Enter name: ").strip()
        pin = input("Enter PIN: ").strip()
        amount = int(input("Enter amount to withdraw: "))
        transaction(name, pin, amount, "withdraw")

    elif choice == "3":  # Deposit money
        name = input("Enter name: ").strip()
        pin = input("Enter PIN: ").strip()
        amount = int(input("Enter amount to deposit: "))
        transaction(name, pin, amount, "deposit")

    elif choice == "4":  # View customers
        print("\n***** Customers & Balances *****")
        for customer, details in customers.items():
            print(f" {customer} | Balance: {details[1]}")
    
    elif choice == "5":  # View mini-statement
        mini_statement()

    elif choice == "6":  # Delete an account
        delete_account()

    elif choice == "7":  # Exit
        print("🚀 Thank you for using our banking system!")
        break

    else:
        print(" Invalid choice! Please try again.")
