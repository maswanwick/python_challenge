import csv

# set data location
budget_data_path = "PyBank\\Resources\\budget_data.csv"

# initializers
total_months = 0
total_profit_or_loss = 0

# open the file
with open(budget_data_path, encoding="UTF-8") as budget_data_csv:
    # obtain reader for the file
    budget_data_reader = csv.reader(budget_data_csv)

    # get header row
    header = next(budget_data_reader)

    # iterate over the data
    for budget_data_record in budget_data_reader:
        total_months += 1
        total_profit_or_loss += int(budget_data_record[header.index("Profit/Losses")])

print(total_months)
print(total_profit_or_loss)
