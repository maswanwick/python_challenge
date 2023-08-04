import csv

# set data location
election_data_path = "PyPoll\\Resources\\election_data.csv"

# initializers
total_vote_count = 0

# open the file
with open(election_data_path, encoding="UTF-8") as election_data_csv:
    election_data_reader = csv.reader(election_data_csv)

    headers = next(election_data_reader)

    for election_data_record in election_data_reader:
        total_vote_count += 1

print(total_vote_count)