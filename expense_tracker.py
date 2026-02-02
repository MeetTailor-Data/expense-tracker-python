expenses = []
def add_expense():
    category = input("Enter Category (Food/Travel/Study/Other): ").strip()
    amount = int(input("Enter Amount: "))
    expense = {
        "Category": category,
        "Amount": amount
    }
    expenses.append(expense)
    print("Expense added successfully!")

def show_expenses():
    if not expenses:
        print("No expenses to show!")
        return
    print("\n--- All Expenses ---")
    for e in expenses:
        print("Category:", e["Category"])
        print("Amount:", e["Amount"])

def category_total():
    if not expenses:
        print("No expenses to calculate!")
        return
    totals = {}
    for e in expenses:
        cat = e["Category"]
        amt = e["Amount"]

        if cat in totals:
            totals[cat] += amt
        else:
            totals[cat] = amt
    print("\n--- Category-wise Total ---")
    for cat, total in totals.items():
        print(cat, ":", total)

def total_expense():
    total = 0
    for e in expenses:
        total += e["Amount"]

    print("Total Expense:", total)

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Category-wise Total")
    print("4. Total Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        category_total()
    elif choice == "4":
        total_expense()
    elif choice == "5":
        print("Exiting Expense Tracker...")
        break
    else:
        print("Invalid Choice! Try again.")
