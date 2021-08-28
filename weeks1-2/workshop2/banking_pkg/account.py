
def show_balance(balance):
    print(f"current Balance: ${balance}")


def deposit(balance):
    amount = int(input("Enter amount to deposit: "))
    return (balance + amount)


def withdraw(balance):
    amount = int(input("Enter amount to withdraw: "))
    if(balance < amount):
        print("Where are you going to ge that kind of money?")
        return balance
    else:
        return (balance - amount)

def logout(name):
    print("Goodbye", name)

def validate_length():
    while True:
        name = input("Enter name to register: ")
        if len(name) in range(1, 10):
            return name
        else:
            print("Name cant be longer than 10 characters")

def validate_pin():
    while True:
        pin = input("Enter PIN: ")
        if len(pin) == 4:
            return pin
        else:
            print("Pin must be 4 numbers!")