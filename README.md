# Python Console Banking System

## 📌 Overview
This is a simple **console-based banking system** written in Python. It simulates basic banking operations like **account creation, deposits, withdrawals, balance inquiry, mini-statements, and account deletion**.

## 🚀 Features
✅ **Open Account** – Create a new account with a secure **4-digit PIN**.
✅ **Deposit Money** – Add funds to your bank account.
✅ **Withdraw Money** – Withdraw funds after PIN authentication.
✅ **Check Balance** – View customer list and their balances.
✅ **Mini-Statement** – View **transaction history** (deposits & withdrawals).
✅ **Delete Account** – Securely remove an account from the system.
✅ **User-Friendly Interface** – Simple menu-driven interaction.
✅ **Error Handling** – Validates PINs, prevents duplicate accounts, and ensures secure transactions.

## 🛠 Requirements
- **Python 3.x** (Make sure it's installed)

## 📥 Installation & Running the Script
1. **Clone the repository (or download the script):**
   ```sh
   git clone https://github.com/Kashavenisruthi/simple-banking-system.git
   cd python-banking-system
   ```
2. **Run the script:**
   ```sh
   python banking_system.py
   ```
   Or, if Python 3 is required:
   ```sh
   python3 banking_system.py
   ```

## 🎯 How to Use
When you run the script, you’ll see the following menu:
```
********* Welcome to State Bank *********
1. Open a New Account
2. Withdraw Money
3. Deposit Money
4. View Customers & Balances
5. View Mini-Statement
6. Delete Account
7. Exit
Enter your choice:
```
Select an option (1-7) to perform banking operations.

### 💡 Example Transactions
#### ➡ **Opening an Account**
```
Enter your choice: 1
Enter full name: John Doe
Set a 4-digit PIN: 1234
Enter initial deposit: 5000
✅ Account created successfully!
```
#### ➡ **Depositing Money**
```
Enter your choice: 3
Enter name: John Doe
Enter PIN: 1234
Enter amount to deposit: 1000
✅ Deposited 1000. New Balance: 6000
```
#### ➡ **Withdrawing Money**
```
Enter your choice: 2
Enter name: John Doe
Enter PIN: 1234
Enter amount to withdraw: 2000
✅ Withdrawn 2000. New Balance: 4000
```
#### ➡ **Viewing Customers & Balances**
```
Enter your choice: 4
***** Customers & Balances *****
👤 John Doe | 💰 Balance: 4000
```
#### ➡ **Viewing Mini-Statement**
```
Enter your choice: 5
📜 Mini-Statement for John Doe:
➡ Account Opened | Initial Deposit: 5000
➡ Deposited: +1000 | Balance: 6000
➡ Withdrawn: -2000 | Balance: 4000
```
#### ➡ **Deleting an Account**
```
Enter your choice: 6
Enter name: John Doe
Enter PIN: 1234
✅ Account deleted successfully!
```

## 📌 Future Enhancements
🔹 **Interest Calculation** – Monthly interest for savings accounts.
🔹 **Loan Processing** – Loan approval & EMI calculations.
🔹 **Graphical User Interface (GUI)** using Tkinter.

## 👨‍💻 Contributing
Pull requests are welcome! Feel free to fork the repo and improve the system.

## 📜 License
This project is open-source and available under the **MIT License**.

🚀 **Happy Banking!**

