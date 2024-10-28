# State Bank - Python Console Banking System

A simple console-based banking system written in Python, simulating basic banking operations like account creation, withdrawal, deposit, and checking customer balances. This project is designed to demonstrate core concepts of Python programming, including input handling, lists, and functions.

## Features

- **Open Account**: Create a new account with a name, a 4-digit PIN, and an initial deposit.
- **Withdraw Money**: Withdraw funds from an account after verifying the correct name and PIN.
- **Deposit Money**: Deposit additional funds into an existing account.
- **Check Customers & Balances**: Display a list of all customers and their current account balances.

## How It Works

The system prompts the user with a menu of options:

1. Open a new account
2. Withdraw money
3. Deposit money
4. Check customers & balances
5. Exit the system

Users can interact with the system by entering their name and PIN for authentication and then performing desired actions such as withdrawing or depositing money.

### Example Workflow

1. **Open Account**: 
   - Input your full name, set a PIN, and deposit an initial amount to create an account.
   
2. **Withdraw Money**:
   - Enter your name, PIN, and withdrawal amount to withdraw funds. The system will check your balance and approve the transaction if sufficient funds are available.
   
3. **Deposit Money**:
   - Enter your name, PIN, and deposit amount to add funds to your account.
   
4. **Check Customers & Balances**:
   - Displays a list of all registered customers and their corresponding balances.

## Usage

Once the program is running, follow the on-screen prompts to interact with the system. You can open new accounts, perform deposits and withdrawals, and check the list of customers with their balances.

### Requirements

- Python 3.10

### Note

This is a simple project for educational purposes. The banking system does not persist data across sessions (data is stored in-memory during runtime only). In a real-world scenario, you would integrate a database and add security measures like encrypted PINs and secure input handling.

## To Do

- Encrypt customer PINs for security.
- Add transaction history tracking for each customer.
- Implement balance inquiry functionality.
- Enhance error handling for edge cases.

## Author

**Shruthi Kashaveni**
