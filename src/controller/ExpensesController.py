import datetime as dt

from db.Database import Database
from setting.RichConsole import RichConsole


class ExpensesController:
    def __init__(self, db_name):
        self.db = Database(db_name)
    def _insert(self,
                    item_price: float,
                    item_name: str,
                    item_amount: int):
        # We need to check if the price is actually valid or not before we insert it into the database
        self.db.insert('INSERT INTO expenses (item_price, item_name, item_amount) VALUES (?, ?, ?)', (item_price, item_name, item_amount))
        return True

    def _fetch(self, table_name='expenses'):
        display = self.db.fetch_all(table_name)
        # Display the data into Rich console
        RichConsole().display(display)

    def _single_fetch(self, id:int ):
        return self.db.fetch_single(id, 'expenses')


    def _delete_single_expense(self, id: int):
        return self.db.delete_single_record(id, 'expenses')

    def _delete_all_expenses(self):
        return self.db.delete_all('expenses')

    def _update_expense(self,id:int,
                item_price: float,
                item_name:str,
                item_amount: int):
        # with self.connection:
        #     set_clauses =[]
        #     data = {"id":id}
        # We check her if any column is updated or not
        self.db.update(id, 'expenses',
                       item_price=item_price,
                       item_name=item_name,
                       item_amount = item_amount)


    def _total(self):
        return self.db.total_expenses('expenses')




