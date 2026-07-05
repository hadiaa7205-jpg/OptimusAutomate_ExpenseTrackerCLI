import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    try:
        amount = float(input("Enter Amount: "))
        category = input("Enter Category: ")
        description = input("Enter Description: ")
        date = input("Enter Date (YYYY-MM-DD): ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("\nExpense Added Successfully!\n")

    except ValueError:
        print("Invalid amount!")


def view_expenses(expenses):
    if not expenses:
        print("\nNo Expenses Found!\n")
        return

    print("\n========== All Expenses ==========\n")

    for i, expense in enumerate(expenses, start=1):
        print(f"Expense #{i}")
        print(f"Amount      : {expense['amount']}")
        print(f"Category    : {expense['category']}")
        print(f"Description : {expense['description']}")
        print(f"Date        : {expense['date']}")
        print("-" * 35)


def delete_expense(expenses):
    if not expenses:
        print("\nNo Expenses Found!\n")
        return

    view_expenses(expenses)

    try:
        number = int(input("\nEnter Expense Number to Delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            save_expenses(expenses)

            print("\nExpense Deleted Successfully!")
            print(f"Deleted: {deleted['description']}")

        else:
            print("Invalid Expense Number!")

    except ValueError:
        print("Please enter a valid number!")


def monthly_summary(expenses):
    if not expenses:
        print("\nNo Expenses Found!\n")
        return

    month = input("\nEnter Month (YYYY-MM): ")

    total = 0
    categories = {}

    for expense in expenses:
        if expense["date"].startswith(month):
            total += expense["amount"]

            category = expense["category"]

            if category in categories:
                categories[category] += expense["amount"]
            else:
                categories[category] = expense["amount"]

    print("\n========== Monthly Summary ==========")
    print(f"Month: {month}")
    print(f"Total Expenses: Rs. {total:.2f}")

    print("\nCategory Wise Expenses:")

    if categories:
        for category, amount in categories.items():
            print(f"{category} : Rs. {amount:.2f}")
    else:
        print("No expenses found for this month.")


expenses = load_expenses()

while True:

    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Monthly Summary")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        delete_expense(expenses)

    elif choice == "4":
        monthly_summary(expenses)

    elif choice == "5":
        print("Good Bye!")
        break

    else:
        print("Invalid Choice!")