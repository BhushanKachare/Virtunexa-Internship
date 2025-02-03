import sqlite3
import datetime
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("finance_tracker.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    type TEXT,
                    category TEXT,
                    amount REAL
                )''')
conn.commit()

def add_transaction(transaction_type):
    """Function to add income or expense"""
    date = datetime.date.today().strftime("%Y-%m-%d")
    category = input("Enter category (e.g., Food, Salary, Bills): ").strip()
    try:
        amount = float(input("Enter amount: "))
        cursor.execute("INSERT INTO transactions (date, type, category, amount) VALUES (?, ?, ?, ?)",
                       (date, transaction_type, category, amount))
        conn.commit()
        print(f"{transaction_type.capitalize()} of ${amount} added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

def view_summary():
    """Function to view monthly income & expense summary"""
    month = input("Enter month (YYYY-MM): ").strip()
    cursor.execute("SELECT type, SUM(amount) FROM transactions WHERE date LIKE ? GROUP BY type", (f"{month}%",))
    results = cursor.fetchall()
    
    if results:
        print("\n📊 Monthly Summary")
        for row in results:
            print(f"{row[0].capitalize()}: ${row[1]:.2f}")
    else:
        print("No records found for this month.")

def generate_report():
    """Function to generate a full report using Pandas"""
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    if not df.empty:
        print("\n📄 Full Financial Report")
        print(df)
        df.to_csv("financial_report.csv", index=False)
        print("Report saved as 'financial_report.csv'")
    else:
        print("No transaction data available.")

def main():
    """Main loop for user interaction"""
    while True:
        print("\n📌 Options: 1) Add Income  2) Add Expense  3) View Summary  4) Generate Report  5) Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_transaction("Income")
        elif choice == "2":
            add_transaction("Expense")
        elif choice == "3":
            view_summary()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            print("Exiting Finance Tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
