class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposit successful!  New Balance: R{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount 
            print(f"Withdraw successful! New Balance: R{self.balance}")
        else:
            print("Transaction Denied: Insufficient funds")

#Safe Guard against automatic exceution
if __name__ == "__main__":
    print("=== Welcome to the Banking Simulator ===")
    name = input("Enter Account Holder Name:")
    initial_deposit = float(input("Enter Initial Deposit Amount: R"))

    #Constructing the user object ('user_account' becomes the 'self' inside the class)
    user_account = BankAccount(account_holder=name, balance=initial_deposit)

    #2. Interactive Runtime Loop 
    while True:
        print("\n What would you like to do?")
        print("1. Check Balance\n2. Deposit Money \n3. Withdraw Money \n4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            #Reading data directly from the object's attributes
            print(f"Current Balance for {user_account.account_holder}: R{user_account.balance}")

        elif choice == '2':
            amount = float(input("Enter deposit ammount: R"))
            user_account.deposit(amount) 
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: R"))
            user_account.withdraw(amount)
        elif choice == '4':
            print("Thank you for banking with Us. GoodBye!")
            break
        else:
            print("Invalid selection. Try again")