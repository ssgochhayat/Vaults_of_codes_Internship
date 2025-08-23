import json
from datetime import datetime


# Function to load expenses from a file
def load_expenses(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Function to save expenses to a file
def save_expenses(expenses, filename):
    with open(filename, 'w') as file:
        json.dump(expenses, file)


# Function to add an expense
def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., Food, Transport): ")
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    expenses.append({"amount": amount, "category": category, "date": date})


# Function to view summary of expenses
def view_summary(expenses):
    total_spending = sum(exp['amount'] for exp in expenses)
    print(f"Total Spending: ${total_spending:.2f}")

    category_summary = {}
    for exp in expenses:
        category_summary[exp['category']] = category_summary.get(exp['category'], 0) + exp['amount']

    for category, total in category_summary.items():
        print(f"Total spending on {category}: ${total:.2f}")


# Main function to run the expense tracker
def main():
    filename = 'expenses.json'
    expenses = load_expenses(filename)

    while True:
        print("-"*50)
        print("Personal Expense Tracker")
        print("-" * 50)
        print("\t 1. Add Expense")
        print("\t 2. View Summary")
        print("\t 3. Exit")
        print("-" * 50)
        choice = input("Choose an option(1-3): ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses, filename)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")
main()


