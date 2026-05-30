
import sys


def check_valid_price(price):
    # Check if the price is actually a number and is positive
    try:
        price = float(price)
        if price is None:
            print('Price cannot be None.')
            return False
        elif not isinstance(price):
            print(f'Invalid price: {price} price must be a number.')
            return False
        elif price <= 0:
            print(f'Invalid price: {price} price must be positive.')
            return False
        return True
    except ValueError:
        print(f'Invalid price: {price} price must be a number.')
        return False



def check_valid_name(name):
    # Check if the name is a valid string
    try:
        name = str(name)
        if name is None:
            print('Name cannot be None.')
            return False
        elif not isinstance(name, str):
            print(f'Invalid name: {name} name must be a string.')
            return False
        elif len(name) == 0:
            print('Invalid name: name cannot be empty.')
            return False
        elif name.isdigit():
            print(f'Invalid name: {name} name cannot be a number.')
            return False
        return True
    except ValueError:
        print(f'Invalid name: {name} name must be a string.')
        return False



def check_valid_amount(amount):
    # Check if the amount is actually a number and is positive
    try:
        amount = int(amount)
        if amount is None:
            print('Amount cannot be None.')
            return False
        elif not isinstance(amount, int):
            print(f'Invalid amount: {amount} amount must be an integer.')
            return False
        elif amount <= 0:
            print(f'Invalid amount: {amount} amount must be positive.')
            return False
        return True

    except ValueError:
        print(f'Invalid amount: {amount} amount must be a number.')
        return False

def only_id(id):
    try:
        id = int(id)
        if id is None or id == '' or id<=0:
            print('ID cannot be None.')
            return False
        elif not isinstance(id, int):
            print(f'Invalid id: {id}')
            return False
        return True
    except ValueError:
        print(f'Invalid id: {id} id must be a number.')
        return False
def menu():

    print("1. Insert Expense")
    print("2. View Expenses")
    print('3. Delete single record')
    print('4. Delete all expenses')
    print('5. Update Expenses')
    print('b: Back to main menu')
    print("6. {q, quit, bye, exit} to Exit")




def back_to_menu(back: str):
    back = str(back)
    if back.lower() in ['back','b','home']:
        return True


def quit(choice):
    quit_lists = ['quit','bye','exit','q']
    if choice.lower() in quit_lists:
        print("Exiting the program. Goodbye!")
        sys.exit(0)

