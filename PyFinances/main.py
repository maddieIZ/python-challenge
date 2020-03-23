
import os
import csv

# open the csv file.

with open('budget_data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    
    
    print('Financial Analysis')
    print('-------------')
    print('Total Month:',len(list(data)))

# delete the header row.

del data[0]

newlist=[]

# create a new list .
for index1 in range(len(data)): 
   newlist.append(data[index1][0])

# create a new list includes the difeerence between current row and next row .
a=[int(newlist[i+1]) - int(newlist[i])   for i in range(len(newlist) -1)]

import operator

# get the maximum value and index and read the max month in the list.

index, value = max(enumerate(a), key=operator.itemgetter(1))
index+1
maxlist = max(a)
maxmonth=[el[1:] for el in data][index+1]
maxmonth=str(maxmonth).replace("[","").replace("]", "")

# get the minimum value and index and read the min month in the list.

minlist = min(a)
index, value = min(enumerate(a), key=operator.itemgetter(1))
index+1
minmonth=[el[1:] for el in data][index+1]
minmonth=str(minmonth).replace("[","").replace("]", "")

# calculate the total .
total = 0
for index1 in range(len(data)):
    total+= int(data[index1][0])

# calculate the average .
average =round (sum(a) / len(a) , 2)

# create the output text file.

results = ( 
f"Financial Analysis \n"
f"-------------\n"
f"Total Month:{len(data)}  \n"
f"-------------\n" 
f"Total: $ {str(total)} \n"
f"Average  Change:${average} \n"
f"Greatest Increase in Profits:{maxmonth} (${maxlist}) \n"
f"Greatest Decrease in Profits:{minmonth} (${minlist}) \n")


create_data = os.path.join('finance_results.txt')
with open(create_data, 'w') as text_file:
    text_writer = text_file.write(results)