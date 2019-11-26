import os
import csv
import collections as ct

csvpath = os.path.join('election_data.csv')

votes = 0
candidate_list = []
candidate_count = []

with open("election_data.csv", "r") as in_file:
    csv_reader = csv.reader(in_file)
    header = next(csv_reader)
   
    for row in csv_reader:
        votes += 1
        candidate = row[2]

        if candidate in candidate_list:
            candidate_index = candidate_list.index(candidate)
            candidate_count[candidate_index] += 1
        else:
            candidate_list.append(candidate)
            candidate_count.append(1)


for e in range(len(candidate_list)):
    print(f'{candidate_list[e]} : {candidate_count[e]}')

print("Total Votes: " + str(votes))
    

# -------------------------------- working-ish ^
#The total number of votes cast
#* A complete list of candidates who received votes
#* The percentage of votes each candidate won
#* The total number of votes each candidate won
#* The winner of the election based on popular vote.





