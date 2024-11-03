# Expense Tracker

A simple command-line expense tracker that allows you to add, view, and delete expenses. This application stores expenses in a list and provides a menu to navigate through different options.

## Features

- **Add Expense**: Enter a name and a positive amount to add an expense.
- **View Expenses**: Lists all added expenses with a running total.
- **Delete Expense**: Remove an expense by specifying its index.
- **Exit**: Close the expense tracker.

## Requirements

- Python 3.x

## Installation

1. Clone the repository (if it's hosted on a version control platform) or download the script.
   
   git clone <repository-url>
   cd <project-directory>

3. (Optional) Set up a virtual environment:
   
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

## Usage

1. Run the script:
   
   python expense_tracker.py
   

2. Follow the menu prompts to add, view, or delete expenses.

## Example Menu


1. Add Expense
2. View Expenses
3. Delete Expense
4. Exit
   
## Error Handling

   Handles invalid inputs, non-integer options, and negative expense amounts.
