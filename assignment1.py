print("Bill Split Calculator")

bill = float(input("Total bill: $"))
while bill <= 0:
    bill = float(input("Must be >0: $"))

people = int(input("Number of people:"))
while people < 1:
        people = int(input("At least 1:"))

tip = input("Tip % (10/15/20/custom): ")
if tip == "custom":
            tip = float(input("Enter %: "))
else:
            tip = float(tip) if tip in ["10","15","20"] else 15

tip_amount = bill * tip / 100
total = bill + tip_amount
each = total / people

print(f"\nSubtotal: ${bill:.2f}")
print(f"Tip: {tip:.0f}%: ${tip_amount:.2f}")
print(f"Total: ${total:.2f}")
print(f"Each person pays: ${each:.2f}")
