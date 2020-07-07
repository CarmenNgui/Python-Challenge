import os
import csv

csvpath = os.path.join('..','Resources','election_data.csv')

total_votes = []
Khan = 0
Correy = 0
Li = 0
Otooley = 0
Khan_percent = 0
Correy_percent = 0
Li_percent = 0
Otooley_percent = 0

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    reader = csv.reader(csvfile)
    next(reader, None)

    for row in reader:
        votes = row[0]
        total_votes.append(votes)
        if row[2] == "Khan":
            Khan = Khan + 1
        elif row[2] == "Correy":
            Correy = Correy + 1
        elif row[2] == "Li":
            Li = Li + 1
        else:
            Otooley = Otooley + 1
total_votes = len(total_votes)

Khan_percent = (Khan / total_votes)*100
Khan_percent = round(Khan_percent,3)
Correy_percent = (Correy / total_votes)*100
Correy_percent = round(Correy_percent,3)
Li_percent = (Li / total_votes)*100
Li_percent = round(Li_percent,3)
Otooley_percent = (Otooley / total_votes)*100
Otooley_percent = round(Otooley_percent,3)

print("Election Results")
print("---------------------")
print(f"Total Votes: {total_votes}")
print("--------------------")
print(f"Khan: {Khan_percent}% ({Khan})")
print(f"Correy: {Correy_percent}% ({Correy})")
print(f"Li: {Li_percent}% ({Li})")
print(f"O'Tooley: {Otooley_percent}% ({Otooley})")
print("--------------------")
print(f"Winner: Khan ")
print("--------------------")

output_file = '../PyPoll/election_results.txt'
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow(f"Khan: {Khan_percent}% ({Khan})")
    csvwriter.writerow(f"Correy: {Correy_percent}% ({Correy})")
    csvwriter.writerow(f"Li: {Li_percent}% ({Li})")
    csvwriter.writerow(f"O'Tooley: {Otooley_percent}% ({Otooley})")
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow([f"Winner: Khan"])
    csvwriter.writerow(["--------------------"])