import os
import csv
import collections as ct

with open("election_data.csv", "r") as in_file:
    csv_reader = csv.reader(in_file)
    header = next(csv_reader)
    rows = [[int(row[0]), row[2]] for row in csv_reader if len(row) > 1]
    votes = 0
    # data = list(csv_reader)

    for row in rows:
        # voter_id = row[0]
        votes += 1

        # candidate = row[-1]
        # votes[candidate] += 1

        # voter_id = row[0]
        # votes[voter_id] += 1
        # sum(votes[voter_id])
    

    print("Total Votes: " + str(votes))

    

#The total number of votes cast
#* A complete list of candidates who received votes
#* The percentage of votes each candidate won
#* The total number of votes each candidate won
#* The winner of the election based on popular vote.

# voting_csv = os.path.join("election_data.csv")

# def vote_counting(vote_data):
#     voter_id = int(vote_data[0])
#     county = str(vote_data[1])
#     candidate = str(vote_data[2])


#     candidate_percent = (candidate/voter_id) * 100

#     print(voter_id)
#     print(candidate_percent)


# with open("election_data.csv","r") as in_file:
#     csv_reader = csv.reader(in_file)
#     header = next(csv_reader)

#     for row in in_file:
#         def total_votes(vote):
#             count = 0
#             for vote in votes:
#                 count = row[0](count + 1)
#             return count
#             print(count)
