print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_per_person = bill / people
tip_per_bill = tip / 100 + 1
pay_per_person = round(bill_per_person * tip_per_bill, 2)
# print(bill_per_person, tip_per_bill, pay_per_person)
# tip_with_bill = tip / 100 * 1
# total_bill = tip_with_bill + bill
# pay_per_person = round(total_bill / people, 2)
# print(f"Each person should pay $" {round((bill / people) * (1 + tip / 100), 2)})
# print(f"Each person should pay ${pay_per_person}.")
print(f"Each person should pay ${pay_per_person}.")