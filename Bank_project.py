C_Names = ["Shruthi", "Jyothi", "Samsritha", "Shirisha", "Harsha", "Varsha"]
C_Pins = ["2199", "9144", "9121", "9703", "8374", "12343"]
C_Balances = [91010, 8110, 57310, 18310, 21710, 63020]
deposite = 0
withdrawal = 0
balance = 0
x = 1
y = 5
i = 0
while True:
    print("****************************************")
    print("    ****Welcome to State Bank****       ")
    print("****************************************")
    print("****  1. Open a new account         ****")
    print("****  2. Withdraw Money             ****")
    print("****  3. Deposit Money              ****")
    print("****  4. Check Customers & Balance  ****")
    print("****  5. Exit/Quit                  ****")
    print("****************************************")
    select=input("Enter a number from above list: ")
    if(select=="1"):
        print("You have selected first choice :)")
        no_of_customers=eval(input("Enter Customers Number:"))
        i=i+no_of_customers
        if i>5:
            print("\nCustomer registration exceed reached or Customer registration too low")
            i = i-no_of_customers
        else:
            while x<= i:
                name=input("Enter a full name:")
                C_Names.append(name)
                pin=str(input("Set a pin:"))
                C_Pins.append(pin)
                balance=0
                deposite=eval(input("Enter money to deposite:"))
                balance=balance+deposite
                C_Balances.append(balance)
                print("\nName=",C_Names[y])
                print("\nPin=", C_Pins[y])
                print("\nBalance=",C_Balances[y])
                x=x+1
                y=y+1
                print("\nYour name,pin and balance are added to Bank's customer list")
                print("****New account created successfully !****")
                print("Note:-- Please remember the Name and Pin")
                print("****************************************")
        Menu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif(select=="2"):
        j = 0
        print("You have selected second choice :)")
        while j < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            while k < len(C_Names)-1:
                k = k + 1
                if name == C_Names[k]:
                    if pin == C_Pins[k]:
                        j = j + 1
                        print("Your Current Balance:", C_Balances[k])
                        balance = (C_Balances[k])
                        withdrawal = eval(input("Input value to Withdraw : "))
                        if balance > withdrawal:
                            balance = balance-withdrawal
                            print("\nWithdraw Successfull!:)")
                            C_Balances[k] = balance
                            print("Your New Balance: ", balance)
                        else:
                            print("Invalid! :) \n  You have entered more than your bank balance. \n Please! Try again")
            if j < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif(select=="3"):
        print("You have selected second choice :)")
        n = 0
        while n < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            while k < len(C_Names) - 1:
                k = k + 1
                if name == C_Names[k]:
                    if pin ==C_Pins[k]:
                        n = n + 1
                        print("Your Current Balance: ",C_Balances[k])
                        balance = (C_Balances[k])
                        deposition = eval(input("Enter the value you want to deposit : "))
                        balance = balance + deposition 
                        C_Balances[k] = balance
                        print("\n****Deposition successful!:)")
                        print("Your New Balance: ", balance)
            if n < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif (select=="4"):
        print("You have selected fourth choice :)")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        while k <= len(C_Names) - 1:
            print("****Customer =", C_Names[k])
            print("****Balance =", C_Balances[k],"\n")
            k = k + 1
        mainMenu = input("Please press enter key to go back to main menu to perform another fuction or exit ...")
    elif (select=="5"):
        print("You have selected fifth choice :)")
        print("Thank you for using our banking system!")
        print("\n")
        break
    else:
        print("Sorry!! :( \n You have been selected invalid option! \n Please! Try again....")
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")

          
