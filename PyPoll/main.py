import os
import csv

csvpath = os.path.join('election_data.csv')

#Variables
votes = 0
candidate_list = []
candidate_count = []
candidate_percent = []

with open("election_data.csv", "r") as in_file:
    csv_reader = csv.reader(in_file)
    header = next(csv_reader)
   
    for row in csv_reader:
        #Adds total number of votes
        votes += 1
        candidate = row[2]

        #If a candidate is in Candidate List, indexes the candidate on Candidate List, finds the index on Candidate Count List, and increases their number of votes by 1
        if candidate in candidate_list:
            candidate_index = candidate_list.index(candidate)
            candidate_count[candidate_index] += 1

        #If a candidate is not in Candidate List, adds candidate to Candidate List, and increases the candidates vote count by 1 on Candidate Count
        else:
            candidate_list.append(candidate)
            candidate_count.append(1)

    #Finds the percent of votes each candidate received, and adds the percentage to the Candidate Percent List
    for e in range(len(candidate_list)):
        vote_percent = round((candidate_count[e]/votes) * 100, 2)
        candidate_percent.append(vote_percent)

    #Finds the Overall Election Winner by finding the candidate listed the maximum amount of times
    winning_candidate = max(candidate_list, key = candidate_list.count)

#Print Results to Terminal

print("_____________________________")
print("      Election Results")
print("_____________________________")
print("Total Votes: " + str(votes))
print("_____________________________")
for e in range(len(candidate_list)):
    print(f'{candidate_list[e]} : {candidate_count[e]} votes : {candidate_percent[e]}%')
print("_____________________________")
print("Winner: " + str(winning_candidate))
print("_____________________________")

#Create and write to Election_Results TXT File

outpath = os.path.join("Election_Results.txt")
txt_file = open("Election_Results.txt", "w")

txt_file.write("_____________________________\n")
txt_file.write("      Election Results\n")
txt_file.write("_____________________________\n")
txt_file.write("Total Votes: " + str(votes))
txt_file.write("\n_____________________________\n")
for e in range(len(candidate_list)):
    txt_file.write(f'{candidate_list[e]} : {candidate_count[e]} votes : {candidate_percent[e]}%\n')
txt_file.write("_____________________________\n")
txt_file.write("Winner: " + str(winning_candidate))
txt_file.write("\n_____________________________")






