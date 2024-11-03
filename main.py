# Initialize an empty list to store expenses
expenses = []

# Main loop for the expense tracker
while True:
    # Display menu options
    print("\n1. Add Expense\n2. View Expenses\n3. Delete Expense\n4. Exit")

    try:
        # Get user choice
        option = int(input("Choose an option: "))
        if option not in [1, 2, 3, 4]:
            print("Please enter a number from 1 to 4.")
            continue  # Repeat menu if input is invalid
    except ValueError:
        print("Enter an integer value.")  # Handle non-integer input
        continue

    if option == 1:
        # Adding a new expense
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

    elif option == 2:
        # Viewing all expenses
        if not expenses:
            print("No expenses found!")  # Check if the list is empty
        else:
            print("\nExpenses:")
            index = 1  # Initialize index for listing expenses
            total = sum(exp['amount'] for exp in expenses)  # Calculate total expenses
            for exp in expenses:
                print(f"{index}. {exp['name']} => ${exp['amount']:.2f}")  # Display each expense
                index += 1  # Increment index
            print(f"Total Amount Spent: ${total:.2f}")  # Display total spent

    elif option == 3:
        # Deleting an expense
        if not expenses:
            print("No expenses.")  # Check if there are no expenses to delete
            continue
        try:
            # Get the index of the expense to delete
            index = int(input("Enter the expense to delete: ")) - 1
            if index < 0 or index >= len(expenses):
                print("Invalid Index.")  # Check for valid index
                continue
            # Remove expense from the list
            removed_expense = expenses.pop(index)
            print(f"Expense '{removed_expense['name']}' deleted successfully.")
        except ValueError:
            print("Enter a valid index.")  # Handle non-integer input for index

    elif option == 4:
        # Exit the tracker
        print("Exiting Tracker.")
        break  # Exit the main loop
