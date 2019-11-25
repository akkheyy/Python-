import os
import csv
import collections as ct

csvpath = os.path.join('election_data.csv')

votes = 0
candidate_list = []
candidate_count = {}


with open("election_data.csv", "r") as in_file:
    csv_reader = csv.DictReader(in_file)
    header = next(csv_reader)
   

    for row in csv_reader:
        votes += 1

        candidate = row["Candidate"]
        
        if candidate not in candidate_list:
        
            candidate_list.append(candidate)

            candidate_count[candidate] = 0

            candidate_count[candidate] = candidate_count[candidate] + 1
            # candidate_votes = candidate_count.get(candidate)

for e in range(len(candidate_list)):
    print(f'{candidate_list} : {candidate_count}')

print("Total Votes: " + str(votes))
    

    

    

#The total number of votes cast
#* A complete list of candidates who received votes
#* The percentage of votes each candidate won
#* The total number of votes each candidate won
#* The winner of the election based on popular vote.





