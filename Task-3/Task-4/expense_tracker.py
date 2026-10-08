import csv
import os

FILE_NAME = "expenses.csv"


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Category", "Amount", "Description"])

        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(" | ".join(row))


def filter_expenses():
    category = input("Enter category to filter: ").lower()

    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        found = False

        for row in reader:
            if row["Category"].lower() == category:
                print(row)
                found = True

        if not found:
            print("No expenses found for this category.")


def category_summary():
    summary = {}

    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            summary[category] = summary.get(category, 0) + amount

    print("\nCategory Summary:")
    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")


while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter by Category")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        filter_expenses()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
