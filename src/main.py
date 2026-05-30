from rich import print

import db.Database as db
from setting.helper import (
    back_to_menu,
    only_id,
    quit,
)
from setting.helper import menu as _menu
from setting.RichConsole import RichConsole

# Validation
from setting.Validation import Validation

validate = Validation()


def _connect_db():
    return db.Database('expenses.db')

def _fetch():
    database = _connect_db()
    expenses = database.fetch_all('expenses')
    RichConsole().display(expenses)

    # for expense in expenses:
    #     print("-" * 100)
    #     created_at = dt.datetime.fromisoformat(expense[4]).strftime('%Y-%m-%d ') if expenses else 'N/A'


def _single_fetch(id: int):
    database = _connect_db()
    return database.fetch_single(id, 'expenses')

def _insert(price :float, name: str, amount: int):
    database = _connect_db()
    return database.insert('INSERT INTO expenses (item_price, item_name, item_amount) VALUES (?, ?, ?)', (price, name, amount))

def _delete_single(id: int):
    database = _connect_db()
    return database.delete_single_record('expenses', id)

def _delete_all():
    database = _connect_db()
    return database.delete_all('expenses')

def _update(id:int, item_price: float, item_name: str, item_amount:float):
    database = _connect_db()
    return database.update(id, 'expenses', item_price=item_price, item_name=item_name, item_amount = item_amount)

def _total():
    database = _connect_db()
    return database.total_expenses('expenses')
if __name__ == '__main__':
    while True:
        _menu()

        choice = input('Enter your choice: ')
        # We need to check if the price is actually valid or not before we insert it into the database
        if quit(choice):
            break

        elif choice == '1':
            try:
                while True:
                    price = input('Enter the price of the item: ')
                    if not validate.validate_price(price, strict=False):
                        print("Please enter a valid price.")
                    else:
                        break
                while True:
                    name = input('Enter the name of the item: ')
                    if not validate.validate_name(name,strict=False):
                        print("Please enter a valid name.")
                    else:
                        break
                while True:
                    amount = input('Enter the amount of the item: ')
                    if not validate.validate_amount(amount,strict=False):
                        print("Please enter a valid amount.")
                    else:
                        break
                _insert(price, name, amount)


            except Exception as err:
                print(f"An error occurred: {err}")

        elif choice == '2':
            _fetch()
            total_exp = _total()
            print(f'Total {total_exp} I have expened so far. ')
        elif choice == '3':
            while True:
                _fetch()
                total_exp = _total()
                print(f'Total {total_exp} I have expened so far. ')
                confirm_delete = input("What ID do you want delete? or press (back/b) to menu: ")
                if back_to_menu(confirm_delete):
                    break

                if only_id(confirm_delete)  :
                    yes_delete = input(f'Are you sure you want delete {confirm_delete}? (yes/no)): ' )
                    if yes_delete.lower()  in ['yes', 'y']:
                        # _fetch()
                        _delete_single(confirm_delete)
                        break
                    elif yes_delete.lower() in ['no', 'n']:
                        # _menu()
                        break
                else:
                    print('Something went wrong! ')

        elif choice == '4':
            # We delete all.
            while True:
                confirm_delete = input("Are you sure delete all? or press (back/b) to menu: ")
                if back_to_menu(confirm_delete):
                    break
                if confirm_delete.lower() in ['yes','y','okay','ok']:
                    _delete_all()
                    break
                    # back_to_menu(confirm_delete)
                else:
                    back_to_menu(confirm_delete)
                    print('Nothing deleted! ')
                    break
        elif choice =='5':

            _fetch()
            total_exp = _total()
            print(f'Total {total_exp} I have expened so far. ')

            while True:
                update_id = input('Which ID do you want to replace? or back to menu (back/b): ')
                if back_to_menu(update_id):
                    break
                if only_id(update_id):

                    # we check if the expenses id actually exists or not
                    if not _single_fetch(int(update_id)):
                        print(f"ID: {update_id} does not exist.")
                        continue

                    # This approach skips the valu.
                    # - Lets say we dont want to update the name only update the price .

                    item_price = input('What is the new price? ')
                    item_name = input('What is the new Item name?  ')
                    item_amount = input('What is the new amount: ')

                    if item_price == '':
                        item_price = None
                    elif not validate.validate_price(item_price, strict=False):
                        continue
                    if item_name == '':
                        item_name =None
                    elif not validate.validate_name(item_name,strict=False):
                        continue
                    if item_amount == '':
                        item_amount = None
                    elif not validate.validate_amount(item_amount, strict=False):
                        continue

                    _update(int(update_id), item_price, item_name, (item_amount))
                    _fetch()
                    total_exp = _total()
                    print(f'Total {total_exp} I have expened so far. ')
                    break
                else:
                    break






        else:
            print("Invalid choice. Please try again.")




