monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input ("Enter your total monthly expenses:"))

monthly_savings = monthly_income - monthly_expenses


#(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).

Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"""
Your monthly savings are ${monthly_savings}.
Projected savings after one year, with interest, is: ${Projected_Savings}.
""")