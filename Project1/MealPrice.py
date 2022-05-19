print("Welcome to MazzBurgers!") 

#Initial values
child_meal_cost = float(input("Enter the cost of the child's meal: $"))
adult_meal_cost = float(input("Enter the cost of the adult's meal: $"))
child_qty = int(input("Enter the number of children: "))
adult_qty = int(input("Enter the number of adults: "))
tax_rate = float(input("Enter the tax rate: %"))
tax_rate_rounded = round(tax_rate, 2)

print()
#Calculations
child_subtotal = child_meal_cost * child_qty
child_subtotal_round= round(child_subtotal, 2)
adult_subtotal = adult_meal_cost * adult_qty
adult_subtotal_round = round(adult_subtotal, 2)
meal_subtotal = child_subtotal_round + adult_subtotal_round

#Aditionals (Drinks and fries)
dirnks_and_fries = input("Would yo like drinks and fries for an aditional $5? (y/n) ")
answer = dirnks_and_fries.upper()

#If statement(tip, drinks and fries)
if(answer == "Y"):
    meal_subtotal += 5
    tip_question = input("Would you like to tip? (y/n) ")
    answer2 = tip_question.upper()
else:
  tip_question = input("Would you like to tip? (y/n) ")
  answer2 = tip_question.upper() 
 

#If statement(tip)
if(answer2 == "Y"): 
  tip_amount = float(input("Enter the tip amount: $"))
  meal_subtotal += tip_amount
  print(f"Subtotal: $ {meal_subtotal:.2f}")    
else:
    print(f"Subtotal: $ {meal_subtotal:.2f}")   
    
  #Costs
tax = ((meal_subtotal * tax_rate_rounded)/100)
tax_round = round(tax, 2)
print(f"Sales Tax: ${tax_round}")
total = meal_subtotal + tax_round
total_round = round(total, 2)
print(f"Total: ${total_round}")
print() 

#Payment
payment = float(input("What is the payment amount: $"))
payment_round = round(payment, 2)
change = payment_round - total_round
change_round = round(change, 2)
print(f"Change: ${change_round}")
print()
print("Thank you for your purchase! Enjoy your meal!")
