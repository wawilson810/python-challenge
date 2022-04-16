from calendar import month
import os
import csv

path = "C:\\Users\\wawil\\python-challenge\\PyBank\\"
budget_csv = os.path.join(path, 'Resources','budget_data.csv')
writepath = path + "analysis\\results.txt"

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    months = []
    net_prof = 0
    prof = []

    for row in csvreader:
        months.append(row[0])
        net_prof+= float(row[1])
        if len(months) == 1:
            prev_prof = float(row[1])
        else:
            prof.append(float(row[1])-prev_prof)
            prev_prof = float(row[1])

    avg_prof = sum(prof)/len(prof)
    max_prof = max(prof)
    min_prof = min(prof)

    for i in range(len(prof)):
        if prof[i] == max_prof:
            max_ind = i+1
        elif prof[i] == min_prof:
            min_ind = i+1

    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${net_prof}")
    print(f"Average Change: ${round(avg_prof, 2)}")
    print(f"Greatest Increase in Profits: {months[max_ind]} (${int(max_prof)})")
    print(f"Greatest Decrease in Profits: {months[min_ind]} (${int(min_prof)})")

with open(writepath, "w") as file:
    lines = ["Financial Analysis", "--------------------------", f"Total Months: {len(months)}", f"Total: ${net_prof}",
    f"Average Change: ${round(avg_prof, 2)}", f"Greatest Increase in Profits: {months[max_ind]} (${int(max_prof)})",
    f"Greatest Decrease in Profits: {months[min_ind]} (${int(min_prof)})"]
    file.write('\n'.join(lines))

