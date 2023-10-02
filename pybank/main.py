import csv 
import os
import numpy as np
csvpath = os.path.join('.','resources','budget_data.csv')
#with open ('./starter_code/pybank/resources/budget_data.csv') as dataset:
with open (csvpath, encoding = 'UTF-8') as dataset:
    csv_iterable = csv.reader(dataset)
    header = next(csv_iterable)
    net_pnl = 0
    months = []
    total_prof = []
    for row in csv_iterable:
        months.append(row[0])
        net_pnl += float(row[1])
        total_prof.append(float(row[1]))
    
    
    diff_col = []
    avgpnlchange = 0
    for num in range(len(total_prof)-1):
        #difference = [b - a for a, b in enumerate(total_diff)]
        diff_col.append((total_prof[num+1] - total_prof[num]))
        avg_pnlchange = sum(diff_col)/len(diff_col)
    
    total_months = len(months)
    avg_pnlchange2 = round(avg_pnlchange, 2)
    max_change = max(diff_col)
    min_change = min(diff_col)
    inc_month = months[diff_col.index(max_change)+1]
    dec_month = months[diff_col.index(min_change)+1]
    print(f'Total months: {total_months}')
    print(f'Total: ${net_pnl}')
    print(f'Average change: ${avg_pnlchange2}')
    print(f'Greatest increase in profits: {inc_month} (${max_change})')
    print(f'Greatest decrease in profits: {dec_month} (${min_change})')

with open('./analysis/Results.csv', 'w') as exportdata:
    exportdata.write("Financial Analysis\n")
    exportdata.write("-------------------------------------------------\n")
    exportdata.write("Total Months: %d\n" % total_months)
    exportdata.write("Total Profits: $%.2f\n" % (net_pnl))
    exportdata.write("Average profit and loss Change $%.2f\n" % avg_pnlchange)
    exportdata.write("Greatest Increase in Profits: %s ($%.2f)\n" % (inc_month,max_change))
    exportdata.write("Greatest Decrease in Profits: %s ($%.2f)\n" % (dec_month,min_change))
