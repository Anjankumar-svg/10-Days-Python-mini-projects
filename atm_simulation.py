pin = 2082
balance = 10000
current_pin = pin

entered_pin = int(input("Enter your pin: "))
if entered_pin == current_pin:
    while True:
        print("1. Check Balance \n2. Withdraw Money \n3. Deposit Money \n4. Change Pin \n5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your balance is:", balance)
        elif choice == 2:
            withdraw_amount = int(input("Enter the amount to withdraw: "))
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print("Withdrawal successful. \nYour new balance is:", balance)
            else:
                print("Insufficient balance.")
        elif choice == 3:
            deposit_amount = int(input("Enter the amount to deposit: "))
            balance += deposit_amount
            print("Deposit successful. \nYour new balance is:", balance)
        elif choice == 4:
            new_pin = int(input("Enter your new pin: "))
            current_pin = new_pin
            print("Pin changed successfully.")
        elif choice == 5:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice.")
else:
    print("Incorrect pin. Access denied.")
