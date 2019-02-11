import os 
import csv

csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline="") as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")

    budget_header = next(budget_data)
   
    # These are the lists in which we will store the data that is necessary to our calculations
    profit_loss = []
    month = []
    value_change = []

    # Loops through the csv file and will calculate the total amount of months and store them in a list
    for row in budget_data:
        profit_loss.append(float(row[1]))
        month.append(row[0])
    
    # This will calculate that total amount of changes there were in the Profit/Loss column
    for i in range(1,len(profit_loss)):
        value_change.append(profit_loss[i]-profit_loss[i-1])

    # Calculating the average change, and the max and min changes
    average_change = sum(value_change)/len(value_change)
    max_change = max(value_change)
    min_change = min(value_change)

    max_change_date = str(month[value_change.index(max(value_change))])
    min_change_date = str(month[value_change.index(min(value_change))])
        
    # Displaying the results       
    print('Financial Analysis')
    print('-----------------------------')
    print(f'Total Months: ', len(month))
    print(f'Total: $', int(sum(profit_loss)))
    print(f'Average Change:',round(average_change,2))
    print(f'Greatest Increase in Profits: ', max_change_date,"($", int(max_change),")")
    print(f'Greatest Decrease in Profits: ', min_change_date,"($", int(min_change),")")

output = open("output.txt", "w")
line1 = "Financial Analysis"
line2 = "-----------------------------"
line3 = str(f"Total Months: {str(month)}")
line4 = str(f"Total: ${profit_loss}")
line5 = str(f"Average Change: ${str(round(average_change,2))}")
line6 = str(f"Greatest Increase in Profits: {max_change_date} (${str(max_change)})")
line7 = str(f"Greatest Decrease in Profits: {min_change_date} (${str(min_change)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
  
