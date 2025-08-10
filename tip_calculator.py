# tip_calculator.py
bill = float(input("Enter total bill: "))
tip_percent = float(input("Enter tip percentage: "))
tip_amount = bill * tip_percent / 100
total = bill + tip_amount
print(f"Tip: ${tip_amount}")
print(f"Total to pay: ${total}")
