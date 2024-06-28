# Personal Finance Manager
#### Video Demo:  <URL HERE>
#### Description:
The Personal Finance Manager is a Python application that helps users manage their finances. It allows users to track their income and expenses, set budgets, and generate financial reports. The application is built with a graphical user interface (GUI) using `tkinter`, and it stores data in an SQLite database.

## Project Files

- **project.py**: This file contains the main logic for the application, including functions to add transactions, populate the transaction view, and generate reports.
- **test_project.py**: This file contains unit tests for the `add_transaction` and `populate_treeview` functions using `pytest`.
- **requirements.txt**: This file lists the required libraries for the project, including `tkinter`, `matplotlib`, `pytest`, and `sqlite3`.

## How to Run
1. Ensure you have Python installed.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the application using `python project.py`.
4. To run tests, use the command `pytest`.

## Design Choices
The project is designed to be user-friendly with a simple GUI. The use of `sqlite3` for data storage ensures that transactions are persistently stored. The application includes functionality for adding and viewing transactions and generating pie chart reports of income and expenses. The modular design allows for easy extension and testing of individual components.
