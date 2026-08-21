class BankAccount:
    def __init__ (self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposit Successful, Deposited R{amount}, New balance is R{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdraw Successful, withdrawn R{amount}, New Balance is R{self.balance}")
        else:
            print("Insufficient Funds!")

if __name__ == "__main__":
    print("=== Welcome to our Banking System===")
    name = input("Enter your User Name: ")
    while True:
        try:
            initial_deposit = float(input("Enter your Initial Deposit: " ))
            break
        except ValueError:
            print("Please Enter a Valid value")
    user_account = BankAccount(account_holder=name, balance=initial_deposit)

    while True:
        print("\n Hello , What would you like to do?")
        print("\n Please select the options below: \n 1: Make deposit \n 2: Make Withdraw \n 3: BalanceInquiry \n 4: ExitService")
        user_input = input("\n Please Enter options From 1-4: "  )
        if user_input == "1":
            while True:
                try:
                    amount = float(input("Please enter the ammount:  "))
                    break
                except ValueError:
                    print("Enter a valid Value")
            user_account.deposit(amount)
        elif  user_input == "2":
            while True:
                try:
                    amount  = float(input("How much would like to withdraw: "))
                    break
                except ValueError:
                    print("Enter a valid Value")
            user_account.withdraw(amount)
        elif user_input == "3":
            print(f"Customer Name: {user_account.account_holder}  Balance  R {user_account.balance}")
        elif user_input == "4":
            print("Thank U for Banking with US ☺")
            break
        else:
            print("Wrong Selection")

        



