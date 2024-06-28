import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def main():
    root = tk.Tk()
    app = FinanceApp(root)
    root.mainloop()

class FinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Manager")

        self.setup_db()
        self.create_widgets()
        self.populate_treeview()

    def setup_db(self):
        self.conn = sqlite3.connect('finance.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                                id INTEGER PRIMARY KEY,
                                type TEXT,
                                category TEXT,
                                amount REAL,
                                date TEXT)''')
        self.conn.commit()

    def create_widgets(self):
        # UI for adding a transaction
        self.type_var = tk.StringVar()
        self.category_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()
        self.date_var = tk.StringVar()

        tk.Label(self.root, text="Type").grid(row=0, column=0)
        tk.OptionMenu(self.root, self.type_var, "Income", "Expense").grid(row=0, column=1)

        tk.Label(self.root, text="Category").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.category_var).grid(row=1, column=1)

        tk.Label(self.root, text="Amount").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.amount_var).grid(row=2, column=1)

        tk.Label(self.root, text="Date (YYYY-MM-DD)").grid(row=3, column=0)
        tk.Entry(self.root, textvariable=self.date_var).grid(row=3, column=1)

        tk.Button(self.root, text="Add Transaction", command=self.add_transaction).grid(row=4, columnspan=2)

        # UI for displaying transactions
        self.tree = ttk.Treeview(self.root, columns=("type", "category", "amount", "date"), show="headings")
        self.tree.heading("type", text="Type")
        self.tree.heading("category", text="Category")
        self.tree.heading("amount", text="Amount")
        self.tree.heading("date", text="Date")
        self.tree.grid(row=5, columnspan=2)

        # UI for generating reports
        tk.Button(self.root, text="Generate Report", command=self.generate_report).grid(row=6, columnspan=2)

    def add_transaction(self):
        type_ = self.type_var.get()
        category = self.category_var.get()
        amount = self.amount_var.get()
        date = self.date_var.get()
        self.cursor.execute("INSERT INTO transactions (type, category, amount, date) VALUES (?, ?, ?, ?)",
                            (type_, category, amount, date))
        self.conn.commit()
        self.populate_treeview()

    def populate_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.cursor.execute("SELECT * FROM transactions")
        for row in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=row[1:])

    def generate_report(self):
        self.cursor.execute("SELECT type, SUM(amount) FROM transactions GROUP BY type")
        data = self.cursor.fetchall()
        if not data:
            messagebox.showinfo("Info", "No data to generate report.")
            return

        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        types = [row[0] for row in data]
        amounts = [row[1] for row in data]
        ax.pie(amounts, labels=types, autopct='%1.1f%%')

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=7, columnspan=2)

if __name__ == "__main__":
    main()
