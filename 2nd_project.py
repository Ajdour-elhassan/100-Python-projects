# Calculator_tip_program
print("welcome to culcultor tip program")
bill = float(input("what was the bill total : $"))
tip = input("how much tip would you like to give? 12 , 10 , or 25 ? ")
people = int(input("how many people to split the bill"))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)