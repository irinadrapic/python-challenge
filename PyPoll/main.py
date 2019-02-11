import os
import csv

election_data = os.path.join("election_data.csv")

#Creating a set of lists to store data that will be needed to make calculations. 
candidates = []
found_votes = []
percent_votes = [] 
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        
        # Counter to calculate how many votes there were
        total_votes += 1 

        # Loop that checks how to see if there is a new value in the candidate row 
        # It will then store the unique value into the candidate list 
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            found_votes.append(1)
        
        #If it has already recognized the name of this candidate it will store its vote in their name
        else:
            index = candidates.index(row[2])
            found_votes[index] += 1
    
    # Adding the values to percent_votes list
    for votes in found_votes:
        percent = (votes/total_votes) * 100
        percent = round(percent)
        percent = "%.3f%%" % percent
        percent_votes.append(percent)
    
    # Calculating the winning candidate
    winner = max(found_votes)
    index = found_votes.index(winner)
    winning_candidate = candidates[index]

# Displaying the election results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(found_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(found_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
    
    




