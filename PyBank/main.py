import csv
import os
import pandas as pd
import numpy as np

# import the location of the file
filepath=os.path.join("Resources","budget_data.csv")

# use pandas to read the csv file
budget_data = pd.read_csv("budget_data.csv")

# Count the number of total months
month = len(budget_data)

#Sum the total profit/loss and format
total = budget_data["Profit/Losses"].sum()
total = '${:.0f}'.format(total)

#Use Diff()to calculate the average change and use mean to calculate the average number
average = budget_data["Profit/Losses"].diff().mean()
average = '${:.2f}'.format(average)


# Add colume to budget_data for the difference
diff=budget_data["Profit/Losses"].diff()
budget_data["Diff"] = diff

#Find the max increase
increase = diff.max()

#Locate the month with max increase
max_increase = budget_data.loc[(budget_data["Diff"]==increase),"Date"].item()
print(max_increase)

#Find the row info of the max decrease
decrease = diff.min()

#Locate the month with max decrease
max_decrease = budget_data.loc[(budget_data["Diff"]==decrease),"Date"].item()

#change the format
increase='${:.0f}'.format(increase)
decrease='${:.0f}'.format(decrease)


print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {month}')
print(f'Total: {total}')
print(f'Average Change: {average}')
print(f'Greatest Increase in Profits: {max_increase} ({increase})')
print(f'Greatest Decrease in Profits: {max_decrease} ({decrease})')

