import csv

# set data location
election_data_path = "PyPoll\\Resources\\election_data.csv"

# initializers
total_vote_count = 0
candidate_data = {}

# open the file
with open(election_data_path, encoding="UTF-8") as election_data_csv:
    election_data_reader = csv.reader(election_data_csv)

    headers = next(election_data_reader)

    for election_data_record in election_data_reader:
        total_vote_count += 1

        candidate_name = election_data_record[headers.index("Candidate")]
        if candidate_name in candidate_data.keys():
            candidate_data[candidate_name] = int(candidate_data[candidate_name]) + 1
        else:
            candidate_data[candidate_name] = 1

print(total_vote_count)
for candidate in candidate_data:
    candidate_vote_count = candidate_data[candidate]
    candidate_percentage = round((candidate_vote_count / total_vote_count) * 100, 3)
    print(candidate, candidate_percentage, candidate_vote_count)