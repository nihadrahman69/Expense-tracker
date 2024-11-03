# Initialize an empty list to store expenses
expenses = []

def display_menu():
    # Display menu options
    print("\n1. Add Expense\n2. View Expenses\n3. Delete Expense\n4. Exit")

def get_option():
    try:
        # Get user choice
        option = int(input("Choose an option: "))
        if option not in [1, 2, 3, 4]:
            print("Please enter a number from 1 to 4.")
            return None
        return option
    except ValueError:
        print("Enter an integer value.")  # Handle non-integer input
        return None

def add_expense():
    name = input("Enter the expense name: ")
    while True:
        try:
            # Get the expense amount
            amount = float(input("Enter the expense amount: "))
            if amount < 0:
                print("Amount can't be negative")  # Reject negative amounts
                continue  # Repeat amount input
            # Add expense to the list
            expenses.append({"name": name, "amount": amount})
            print(f"Expense '{name}' of ${amount:.2f} added successfully.")
            break  # Exit amount input loop
        except ValueError:
            print("Enter a valid number for the amount.")  # Handle non-numeric input

def view_expenses():
    # Viewing all expenses
    if not expenses:
        print("No expenses found!")  # Check if the list is empty
    else:
        print("\nExpenses:")
        total = 0  # Initialize total for calculating total expenses
        for index, exp in enumerate(expenses, start=1):
            print(f"{index}. {exp['name']} => ${exp['amount']:.2f}")  # Display each expense
            total += exp['amount']
        print(f"Total Amount Spent: ${total:.2f}")  # Display total spent

def delete_expense():
    # Deleting an expense
    if not expenses:
        print("No expenses.")  # Check if there are no expenses to delete
        return
    try:
        # Get the index of the expense to delete
        index = int(input("Enter the expense to delete: ")) - 1
        if 0 <= index < len(expenses):
            removed_expense = expenses.pop(index)
            print(f"Expense '{removed_expense['name']}' deleted successfully.")
        else:
            print("Invalid Index.")  # Check for valid index
    except ValueError:
        print("Enter a valid index.")  # Handle non-integer input for index

# Main loop for the expense tracker
while True:
    display_menu()
    option = get_option()
    if option is None:
        continue
    elif option == 1:
        add_expense()
    elif option == 2:
        view_expenses()
    elif option == 3:
        delete_expense()
    elif option == 4:
        # Exit the tracker
        print("Exiting Tracker.")
        break  # Exit the main loop
