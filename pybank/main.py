import csv 
import os
#csv path makes an object from the path of the file
csvpath = os.path.join('.','starter_code','pybank','resources','budget_data.csv')
#with open ('./starter_code/pybank/resources/budget_data.csv') as dataset:

#With opens file using the cvs module
with open (csvpath, encoding = 'UTF-8') as dataset:
    csv_iterable = csv.reader(dataset) # creates an iterable object from the dataset
    header = next(csv_iterable) #Separates the headers from the rest of the data, allowing to make calculations
    
    #Sets variables, to take in values as a cumulative value and lists respectively
    net_pnl = 0
    months = []
    total_prof = []

    #For loop that fills the lists with column 0 and column 1 respectively iterating till the end row of teh dataset and sums the pnl of every month
    for row in csv_iterable:
        months.append(row[0])
        net_pnl += float(row[1])
        total_prof.append(float(row[1]))
    
    diff_col = []  #Creates another list for calculations
    avgpnlchange = 0

    '''
    For loop to iterate through the months and total profit and losses list and calculate the difference between the next row and current row...
    and adds them to the end of the calculations list (diff_col)
    '''
    for num in range(len(total_prof)-1):
        
        diff_col.append((total_prof[num+1] - total_prof[num]))
        avg_pnlchange = sum(diff_col)/len(diff_col)
    #Calculations for the total number of months, maximum and minimum pnl change and the respective month for each change 
    total_months = len(months)
    avg_pnlchange2 = round(avg_pnlchange, 2) #rounds up to 2 decimals
    max_change = max(diff_col)
    min_change = min(diff_col)
    inc_month = months[diff_col.index(max_change)+1] # Uses the position of the change value to look for the month
    dec_month = months[diff_col.index(min_change)+1]
   
   #Output results
    print(f'Total months: {total_months}')
    print(f'Total: ${net_pnl}')
    print(f'Average change: ${avg_pnlchange2}')
    print(f'Greatest increase in profits: {inc_month} (${max_change})')
    print(f'Greatest decrease in profits: {dec_month} (${min_change})')

#Exports and string formats the results to a new csv file
with open('./analysis/Results.txt', 'w') as exportdata:
    exportdata.write("Financial Analysis\n")
    exportdata.write("-------------------------------------------------\n")
    exportdata.write("Total Months: %d\n" % total_months)
    exportdata.write("Total Profits: $%.2f\n" % (net_pnl))
    exportdata.write("Average profit and loss Change $%.2f\n" % avg_pnlchange)
    exportdata.write("Greatest Increase in Profits: %s ($%.2f)\n" % (inc_month,max_change))
    exportdata.write("Greatest Decrease in Profits: %s ($%.2f)\n" % (dec_month,min_change))
