expenses = []

def add_expense():
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount <= 0:
                print("Amount must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    category = input("Enter expense category (e.g., food, transportation, entertainment): ").strip()
    description = input("Enter expense description: ").strip()

    expense = {
        'amount': amount,
        'category': category,
        'description': description
    }
    expenses.append(expense)
    print("Expense added successfully.")

def display_summary():
    summary = {}
    for expense in expenses:
        category = expense['category']
        if category not in summary:
            summary[category] = 0
        summary[category] += expense['amount']
    
    if not summary:
        print("No expenses recorded.")
    else:
        for category, total in summary.items():
            print(f"Category: {category}, Total Spent: ${total:.2f}")

while True:
    print("\n1. Add Expense")
    print("2. View Summary")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ").strip()
    
    if choice == '1':
        add_expense()
    elif choice == '2':
        display_summary()
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
