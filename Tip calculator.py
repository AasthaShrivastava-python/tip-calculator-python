print("Welcome to the tip calculator!")
total_bill =float(input("your total bill :"))
tip = float(input("how much tip would you like to give :"))
bill_split =float(input("how many people are going to split the bill :"))
(total_bill/bill_split)
tip_percent = (tip/100)
total_tip = (total_bill * tip_percent)
amount = (total_bill + total_tip)
split_amount = (amount/bill_split)

print(f"the amount each person will have to pay is : {split_amount:.2f}")
print("thank you for visiting!\n please visit again!\n")
input("Press Enter to exit....")









