import csv

# set data location
election_data_path = "PyPoll\\Resources\\election_data.csv"
analysis_data_path = "PyPoll\\analysis\\pypoll_analysis.txt"

# creates a new file with no content, so we can append to it with our summary data
def create_analysis_file():
    f = open(analysis_data_path, "w")
    f.close()

# appends the summary data line to the analysis file as well as prints it to the console
def write_content(content):
    # append to analysis file
    with open(analysis_data_path, "a") as analysis_file:
        analysis_file.write(f"{content}\n")
    
    # print to console
    print(content)

# helper method to write the analysis seperator content
def write_seperator():
    write_content("-------------------------")

# initializers
total_vote_count = 0
winning_vote_total = 0
candidate_data = {}
winning_candidate = ""

# main logic section

# open the file
with open(election_data_path, encoding="UTF-8") as election_data_csv:
    # obtain reader for the file
    election_data_reader = csv.reader(election_data_csv)

    # get the header row
    headers = next(election_data_reader)

    # iterate over the data
    for election_data_record in election_data_reader:
        # increment the total vote count
        total_vote_count += 1

        # retrieve the candidate name for the record
        candidate_name = election_data_record[headers.index("Candidate")]

        # if the candidate is in the dictonary already, increment the candidate's vote count by 1
        # if they are not in the dictionary, add them with a vote count value of 1
        if candidate_name in candidate_data.keys():
            candidate_data[candidate_name] = int(candidate_data[candidate_name]) + 1
        else:
            candidate_data[candidate_name] = 1

# report our findings

# create an empty file to hold our analysis
create_analysis_file()

# print the content to the analysis file and the console
write_content("Election Results")
write_seperator()
write_content(f"Total Votes: {total_vote_count}")
write_seperator()

# iterate over each entry in the dictionary
# capture the candidate's vote total and calculate the percentage of total votes
for candidate in candidate_data:
    candidate_vote_count = candidate_data[candidate]
    candidate_percentage = round((candidate_vote_count / total_vote_count) * 100, 3)
    write_content(f"{candidate}: {candidate_percentage}% ({candidate_vote_count})")

    # determine which candidate had the most votes by keeping track of the high mark
    if (candidate_vote_count > winning_vote_total):
        winning_vote_total = candidate_vote_count
        winning_candidate = candidate

write_seperator()
write_content(f"Winner: {winning_candidate}")
write_seperator()
