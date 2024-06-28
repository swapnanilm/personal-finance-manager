import pytest
import sqlite3
from project import add_transaction, setup_db, populate_treeview

def test_add_transaction():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    setup_db(cursor)
    add_transaction(cursor, 'Income', 'Salary', 5000, '2024-06-01')
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    assert len(rows) == 1
    assert rows[0][1] == 'Income'
    assert rows[0][2] == 'Salary'
    assert rows[0][3] == 5000

def test_populate_treeview():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    setup_db(cursor)
    add_transaction(cursor, 'Expense', 'Groceries', 100, '2024-06-01')
    transactions = populate_treeview(cursor)
    assert len(transactions) == 1
    assert transactions[0][1] == 'Expense'
    assert transactions[0][2] == 'Groceries'
    assert transactions[0][3] == 100

