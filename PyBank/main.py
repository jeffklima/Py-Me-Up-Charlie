import os
import csv

budget_csv = os.path.join("Resources/budget_data.csv")

with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    profit = []
    date = []
    profit_change = []

    #The net total amount of "Profit/Losses" over the entire period
    for row in csvreader:
        profit.append(float(row[1]))
        
    #The total number of months included in the dataset
        date.append(row[0])

    #The average of the changes in "Profit/Losses" over the entire period
    for i in range(1,len(profit)):
        profit_change.append(profit[i] - profit[i-1])   
        avg_change = sum(profit_change)/len(profit_change)
        
        #The greatest increase in profits (date and amount) over the entire period   
        max_change = max(profit_change)
        max_change_date = str(date[profit_change.index(max(profit_change))])

        #The greatest decrease in losses (date and amount) over the entire period
        min_change = min(profit_change)     
        min_change_date = str(date[profit_change.index(min(profit_change))])

    print("Financial Analysis")
    print("-----------------------------")
    print("Total Months:", len(date))
    print("Total: $", sum(profit))
    print("Avereage Change: $", round(avg_change, 2))
    print("Greatest Increase in Profits:", max_change_date,"($",max_change,")")
    print("Greatest Decrease in Profits:", min_change_date,"($",min_change,")")