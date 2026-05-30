import datetime as dt

from rich.console import Console
from rich.table import Table


class RichConsole:
    def __init__(self):
        self.console = Console()

    def display(self, expenses):
        table = Table(title="Expenses", show_lines=True)
        table.add_column("ID")
        table.add_column("Price")
        table.add_column("Name")
        table.add_column("Amount")
        table.add_column("Date")

        for expense in expenses:
            created_at = dt.datetime.fromisoformat(expense[4]).strftime('%Y-%m-%d ') if expenses else 'N/A'
            table.add_row(
                str(expense[0]),
                f"{expense[1]}",
                str(expense[2]),
                str(expense[3]),
                created_at
            )

        self.console.print(table)
