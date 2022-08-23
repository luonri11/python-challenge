import os
import csv

from bitarray import test
rowcount = 0
total = 0

change = 0
profit=0

test_variable=0

change_list = []
budget_csv = os.path.join("Resources", "budget_data.csv")



#open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    header = next(csv_reader)
    
    for x in csv_reader:
       rowcount = rowcount+1
       total = (total + float(x[1]))
       
       

print("Financial Analysis")
print("-------------------------------------------")
print(f"Total Months: {rowcount}")
print(f"Total: ${total}")

#print(f"Average Change List: {change_list}")


  
