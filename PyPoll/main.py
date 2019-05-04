import os
import csv

election_csv = os.path.join("Resources/election_data.csv")

poll = {}
total_votes = 0
candidates = []
number_votes = []
vote_percent = []
winner_list = []

with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #The total number of votes cast
    for row in csvreader:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1

#A complete list of candidates who received votes
#The total number of votes each candidate won
for key, value in poll.items():
    candidates.append(key)
    number_votes.append(value)   

# The percentage of votes each candidate won
for n in number_votes:
    vote_percent.append(round(n/total_votes*100, 1))

# Make into tuples
clean_data = list(zip(candidates, number_votes, vote_percent))

#The winner of the election based on popular vote
for name in clean_data:
    if max(number_votes) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]

#Export text file
output_path = os.path.join("Output", "election_results.txt")

#Prints to terminal
print('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
    '\n-------------------------\n')
for entry in clean_data:
    print(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
print('------------------------- \nWinner: ' + winner + '\n-------------------------')

with open(output_path, 'w') as txtfile:
    txtfile.write('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.write(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.write('------------------------- \nWinner: ' + winner + '\n-------------------------')
