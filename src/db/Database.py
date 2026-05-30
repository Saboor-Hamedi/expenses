from sqlite3 import connect


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = connect(self.db_name)
        self._create_table()

    def _create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_price REAL NOT NULL,
                    item_name TEXT NOT NULL,
                    item_amount INTEGER NOT NULL,
                    created_at DEFAULT CURRENT_TIMESTAMP,
                    updated_at DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            # alter table add index

    def insert(self, query, params):
        try:
            with self.connection:
                    if query and params:
                        cursor  = self.connection.execute(query, params)
                        if cursor.rowcount >0:
                            print("Data inserted successfully.")
                        else:
                            print("No data inserted.")
                    else:
                        print("Invalid query or parameters.")
                        # self.connection.execute(query, params)

        except Exception as err:
            print(f"Something happend while inserting data: {err}")
    def fetch_all(self,table_name='expenses'):
        try:
            with self.connection:
                if self._amount(table_name) == 0:
                    print("No data found.")
                    return []
                cursor = self.connection.execute(f"SELECT * FROM {table_name}")
                return cursor.fetchall()

        except Exception as err:
            print(f"Something happend while fetching data: {err}")
            return[]

    def fetch_single(self, id:int, table_name):
        with self.connection:
            cursor = self.connection.execute(f'SELECT * FROM {table_name} WHERE id = ?', (id,))
            return cursor.fetchone()


    def delete_all(self, table_name='expenses'):
        try:
            with self.connection:
                cursor = self.connection.execute(f"DELETE FROM {table_name}")
                if cursor.rowcount > 0:
                    print("Data deleted successfully.")
                else:
                    print("No data found to delete.")
        except Exception as err:
            print(f"Something happend while deleting data: {err}")

    def delete_single_record(self, id:int, table_name='expenses'):
        # try:
        with self.connection:
            cursor = self.connection.execute(f"DELETE FROM {table_name} WHERE id = ?", (id,))
            if cursor.rowcount > 0:
                print("Data deleted successfully.")
            else:
                print("No data found to delete.")

        # except Exception as err:
        #     print(f"Something happend while deleting data: {err}")
        #     return False

    def update(self, id:int, table_name:str, item_price: float, item_name:str, item_amount: int):
        with self.connection:
            set_clauses =[]
            data = {"id":id}

            # We check her if any column is updated or not
            if item_price is not None:
                set_clauses.append("item_price = :item_price")
                data['item_price'] = item_price
            if item_name is not None:
                set_clauses.append("item_name = :item_name")
                data['item_name'] = item_name
            if item_amount is not None:
                set_clauses.append("item_amount = :item_amount")
                data['item_amount'] = item_amount
            set_clause= ', ' .join(set_clauses)

            query = f"UPDATE {table_name} SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE id = :id"


            cursor = self.connection.execute(query,data)
            if cursor.rowcount > 0:
                print('Expenses updated successfully. ')
            else:
                print('Nothing has changed. ')
    def _amount(self,table_name):
        with self.connection:
            cursor = self.connection.execute(f"SELECT COUNT(id) FROM {table_name}")
            return cursor.fetchone()[0]

    def total_expenses(self, table_name='expenses'):
        with self.connection:
            cursor = self.connection.execute(f'SELECT SUM(item_price * item_amount) FROM {table_name}')
            return cursor.fetchone()[0] or 0



