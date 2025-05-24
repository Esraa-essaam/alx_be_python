the_income = int(input("Enter your monthly income:"))
total_expenses = int(input ("Enter your total monthly expenses:"))

monthly_savings = total_expenses - the_income 

#(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).

Projected_Savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"""
Your monthly savings are ${monthly_savings}.
Projected savings after one year, with interest, is: ${Projected_Savings}.
""")