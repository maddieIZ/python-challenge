#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# read the csv file to a dictionary:


fn = 'houston_election_data - Copy.csv'

with open(fn, encoding="utf-8-sig")  as f:
    csv = csv.DictReader(f)



#read csv file to a list:


import csv

messages = []
with open('houston_election_data - Copy.csv', encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        messages.append(row)


# count the candidatea , chack if the candidate name exist in our list then add 1 , if not create the name with 1 as count.

results = {}
Firstresults = {}


for row in messages:
    name = row['Candidate']
    
    if name not in results:
        results[name] = 1
        Firstresults [name] = 1
    else:
        results[name]+= 1
        Firstresults[name]+= 1

# number of votes .

tot=len(messages)

# calculate percentage.
#  
for i in results:    
    results[i] =round(100*results[i] / tot , 1)



import operator
sorted_d ={}



sorted_d = dict( sorted(results.items(), key=operator.itemgetter(1),reverse=True))
sorted_d2 = dict( sorted(Firstresults.items(), key=operator.itemgetter(1),reverse=True))


# add percentage sign .

for key,value in sorted_d.items():
   sorted_d[key] = str(value) + '%'



dic1 = sorted_d
dic2 = sorted_d2
tt = {}

for key in (dic1.keys() | dic2.keys()):
    if key in dic1: tt.setdefault(key, []).append(dic1[key])
    if key in dic2: tt.setdefault(key, []).append(dic2[key])

sorted_d = dict( sorted(tt.items(), key=operator.itemgetter(1),reverse=True))


results = ( 
f"Houston Mayoral Election Results \n"
f"-------------\n"
f"Total Cast Votes:{len(messages)}  \n"
f"-------------\n " )

# create text file.

create_data = os.path.join('election_results.txt')
with open(create_data, 'w') as text_file:
    text_writer = text_file.write(results)

# add to txt file.


with open(create_data, "a+") as text_file:
    for k,v in sorted_d.items():
          text_file.write("\n")
          text_writer = text_file.write(str(k).replace("[","").replace("]", "") +': '  + str(v).replace("[","").replace("]", ""))

for x in list(sorted_d)[0:1]:
    with open(create_data, "a+") as text_file:
       text_file.write("\n") 
       results3 = ( 
            f"-------------\n "
            f"1st Advancing Candidate:{x}  \n"
            f"-------------\n " ) 
       text_writer = text_file.write(results3)

for y in list(sorted_d)[1:2]:
    with open(create_data, "a+") as text_file:
       results2 = ( 
            f"2st Advancing Candidate:{y}  \n"
            f"-------------\n " ) 
       text_writer = text_file.write(results2)







