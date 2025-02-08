import json
import os
from datetime import datetime

# Define the file where expenses will be stored
data_file = "expenses.json"

def load_data():
    """Load expenses from the JSON file if it exists, otherwise return an empty list."""
    print("Loading data from file...")
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            data = json.load(file)
            print("Data loaded successfully.")
            return data
    print("No existing data found.")
    return []

def save_data(data):
    """Save the expense data to the JSON file."""
    print("Saving data to file...")
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)  # Writing JSON data with indentation for readability
    print("Data saved successfully.")

def add_expense():
    """Prompt the user to input expense details and save them."""
    try:
        amount = float(input("Enter expense amount: "))  # Convert input to float for calculations
        description = input("Enter description: ")  # Short note about the expense
        category = input("Enter category (e.g., Food, Transport, Entertainment): ")  # Categorize expense
        date = datetime.now().strftime("%Y-%m-%d")  # Capture current date
        
        print("Adding expense...")
        expenses = load_data()  # Load existing expenses from file
        expenses.append({"date": date, "amount": amount, "description": description, "category": category})
        save_data(expenses)  # Save updated expense list back to file
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a numeric value for amount.")

def view_expenses():
    """Display all recorded expenses."""
    print("Fetching all recorded expenses...")
    expenses = load_data()
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("\nExpense Records:")
    for expense in expenses:
        print(f"{expense['date']} - {expense['category']} - {expense['description']}: ${expense['amount']}")
    print("Displayed all expenses.")

def expense_summary():
    """Provide a summary of expenses categorized by type."""
    print("Generating expense summary...")
    expenses = load_data()
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    summary = {}
    for expense in expenses:
        category = expense['category']
        summary[category] = summary.get(category, 0) + expense['amount']  # Summing up expenses by category
    
    print("\nExpense Summary:")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")  # Display category-wise total expenses
    print("Expense summary displayed.")

def main():
    """Main function to handle user interaction."""
    print("Starting Expense Tracker...")
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Expense Summary")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        print(f"User selected option {choice}")
        if choice == "1":
            add_expense()  # Call function to add new expense
        elif choice == "2":
            view_expenses()  # Call function to display all expenses
        elif choice == "3":
            expense_summary()  # Call function to generate summary report
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")
    print("Expense Tracker closed.")

if __name__ == "__main__":
    main()  # Run the main function if script is executed directly

