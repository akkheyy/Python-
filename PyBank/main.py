import os
import csv
import collections as ct

with open("budget_data.csv", "r") as in_file:
    csv_reader = csv.reader(in_file)
    header = next(csv_reader)
    votes = ct.Counter()

    for row in csv_reader:
        voter_id = row[0]
        votes[voter_id] += 1
    

    print(votes)
    print(votes[voter_id])



    # data = list(csv_reader)

    # clean_data = [[int(e) for e in row[1]] for row in data[1]]

    # # clean_data = [[int(e) for e in row[1]] for row[1] in data]

    # greatest_increase = max(data, key=lambda row: row[1])

    
    # print(greatest_increase)

    # greatest_decrease = min(data, key=lambda row: row[2])

    # print(greatest_decrease)


  

    #1997 rows

    
   

    # for row in csv_reader:
    #     total_months = [row[0]for row in csv_reader]
    #     print(total_months)

   



