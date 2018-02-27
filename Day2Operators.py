meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
Tip = meal_cost * tip_percent / 100
Tax = meal_cost * tax_percent / 100
Total_Meal = round(Tip + Tax + meal_cost)

print('The total meal cost is ' + str(Total_Meal) + ' dollars.')