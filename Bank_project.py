C_Names = ["Shruthi", "Jyothi", "Samsritha", "Shirisha", "Harsha", "Varsha"]
C_Pins = ["2199", "9144", "9121", "9703", "8374", "12343"]
C_Balances = [91010, 8110, 57310, 18310, 21710, 63020]

def find_customer_index(name, pin):
    """Find the index of a customer given their name and pin."""
    if name in C_Names:
        index = C_Names.index(name)
        if C_Pins[index] == pin:
            return index
    return None

def open_account():
    """Open a new account."""
    global C_Names, C_Pins, C_Balances
    try:
        no_of_customers = int(input("Enter the number of customers to register: "))
        if no_of_customers <= 0:
            print("Number of customers must be greater than zero.")
            return

        for _ in range(no_of_customers):
            name = input("Enter a full name: ")
            pin = input("Set a pin: ")
            deposit = float(input("Enter amount to deposit: "))
            C_Names.append(name)
            C_Pins.append(pin)
            C_Balances.append(deposit)
            print(f"Account created successfully!\nName: {name}\nPin: {pin}\nBalance: {deposit}")
    except ValueError:
        print("Invalid input! Please enter numeric values for the number of customers and deposit amount.")

def withdraw_money():
    """Withdraw money from an account."""
    name = input("Enter your name: ")
    pin = input("Enter your pin: ")
    index = find_customer_index(name, pin)
    if index is not None:
        try:
            withdrawal_amount = float(input("Enter amount to withdraw: "))
            if withdrawal_amount <= 0:
                print("Withdrawal amount must be positive.")
                return
            if withdrawal_amount <= C_Balances[index]:
                C_Balances[index] -= withdrawal_amount
                print(f"Withdrawal successful! New balance: {C_Balances[index]}")
            else:
                print("Insufficient balance.")
        except ValueError:
            print("Invalid input! Please enter a numeric value for the withdrawal amount.")
    else:
        print("Invalid name or pin.")

def deposit_money():
    """Deposit money into an account."""
    name = input("Enter your name: ")
    pin = input("Enter your pin: ")
    index = find_customer_index(name, pin)
    if index is not None:
        try:
            deposit_amount = float(input("Enter amount to deposit: "))
            if deposit_amount <= 0:
                print("Deposit amount must be positive.")
                return
            C_Balances[index] += deposit_amount
            print(f"Deposit successful! New balance: {C_Balances[index]}")
        except ValueError:
            print("Invalid input! Please enter a numeric value for the deposit amount.")
    else:
        print("Invalid name or pin.")

def check_customers():
    """Display all customers and their balances."""
    print("Customer list and balances:")
    for i in range(len(C_Names)):
        print(f"Name: {C_Names[i]}, Balance: {C_Balances[i]}")

def main():
    while True:
        print("\n****************************************")
        print("    **** Welcome to State Bank ****      ")
        print("****************************************")
        print("****  1. Open a new account         ****")
        print("****  2. Withdraw Money             ****")
        print("****  3. Deposit Money              ****")
        print("****  4. Check Customers & Balance  ****")
        print("****  5. Exit/Quit                  ****")
        print("****************************************")
        
        selection = input("Enter a number from the list above: ")
        
        if selection == "1":
            open_account()
        elif selection == "2":
            withdraw_money()
        elif selection == "3":
            deposit_money()
        elif selection == "4":
            check_customers()
        elif selection == "5":
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid selection! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
