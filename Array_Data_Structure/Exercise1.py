MonthlyExpense = [2200, 2350, 2600, 2130, 2190]
# 1. In Feb, how many dollars you spent extra compare to January?
print("In Feb, this is how much I spent extra compare to Jan: ",MonthlyExpense[1] - MonthlyExpense[0]);
#2. Find out your total expense in first quarter (first three months) of the year
Total_Expense = MonthlyExpense[0] + MonthlyExpense[1] + MonthlyExpense[2]
print("This is how much the total expense came up to be in the first quarter:",Total_Expense)
# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spend $2000 dollars in any month?", 2000 in MonthlyExpense)
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
MonthlyExpense.append(1980)
print(MonthlyExpense)
#5. You returned an item that you bought in a month of April and 
#got a refund of 200$. Make a correction to your monthly expense list
#based on this
MonthlyExpense[3] = MonthlyExpense[3] - 200
print(MonthlyExpense[3])
print(MonthlyExpense)



