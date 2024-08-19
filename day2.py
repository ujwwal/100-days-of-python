#tip caclulator
print("We are going to calculate the tip!")
bill = float(input("Enter the bill amount: $"))
tip = float(input("Enter the % of the tip you want to give: "))
calculated_tip = (bill*tip)/100
question = input("Do you want to split the bill? (Y/N): ")
if question == "Y":
	print("so you have decided to split the bill.. hmmm \n")
	people = int(input("Enter the nmber of people: \n"))
	splitted_bill = (bill+calculated_tip)/people
	print(f"Each person should pay $", splitted_bill)
	
else:
	print("goodbye have a nice day!")
		
	
