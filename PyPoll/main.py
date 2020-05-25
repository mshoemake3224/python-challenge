import os
import csv

csvpath = os.path.join('..', 'PyPoll',"Resources", 'election_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    candidate = []
    total_votes = 0
    candidate_total = 0
    votes_per_candidate = []
    percentage_votes = []
    header = next(csvreader)

    for x in csvreader:
        # The total number of votes cast
        total_votes = total_votes + 1
print ("Election Results")
print ("--------------------------")
print ("Total Votes:" , total_votes)
print ("--------------------------")


# A complete list of candidates who received votes
        if x[2] not in candidate:
            candidate.append(x[2])
        print (candidate)


# The total number of votes per candidate
        if x[2] in candidate:
             candidate_index = x[2].index(candidate)
             votes_per_candidate[candidate_index] = votes_per_candidate[candidate_index] + 1

# The percentage of votes each candidate won
        for x in range(len(x[2])):
            vote_percent = votes_per_candidate[x]/total_votes*100
            percentage_votes.append(vote_percent)

            leading_candidate = votes_per_candidate[x]
            if votes_per_candidate[x] > leading_candidate:
                leading_candidate = votes_per_candidate[x]
                index = x
# The winner of the election based on popular vote
        winner = candidate[index]


output_file = os.path.join("pypoll_results.txt")
with open(output_file, "w",newline="") as datafile:
    datafile.write("--------------------------------------------------")
    datafile.write("Election Results")
    datafile.write("---------------------------------------------------")
    datafile.write(f"Total Votes: {total_votes}")
    datafile.write("---------------------------------------------------")

    for x in range(len(candidate)):
        datafile.write(f"{candidate[x]} : {percentage_votes[x]}% ({votes_per_candidate[x]})")
    datafile.write("---------------------------------------------------")")
    datafile.write(f"Winner: {winner.upper()}"")
    datafile.write("---------------------------------------------")")



# Example of Output:
    # Election Results
    # -------------------------
    # Total Votes: 3521001
    # -------------------------
    # Khan: 63.000% (2218231)
    # Correy: 20.000% (704200)
    # Li: 14.000% (492940)
    # O'Tooley: 3.000% (105630)
    # -------------------------
    # Winner: Khan
    # -------------------------
