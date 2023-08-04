import csv

# set data location
budget_data_path = "PyBank\\Resources\\budget_data.csv"

# initializers
total_months = 0
total_profit_or_loss = 0
prev_profit_or_loss = 0
profit_changes = []


# open the file
with open(budget_data_path, encoding="UTF-8") as budget_data_csv:
    # obtain reader for the file
    budget_data_reader = csv.reader(budget_data_csv)

    # get header row
    header = next(budget_data_reader)

    # iterate over the data
    for budget_data_record in budget_data_reader:
        # increment the month total
        total_months += 1

        # get the current record's profit/loss value
        current_profit_or_loss = int(budget_data_record[header.index("Profit/Losses")])

        # increment the total profit of loss total
        total_profit_or_loss += int(current_profit_or_loss)

        # if this isn't the first month, subtract the current profit/loss from the last profit/loss
        # to get the monthly change.  Store that in profit changes list
        if (total_months > 1):
            profit_changes.append(current_profit_or_loss - prev_profit_or_loss)
        
        # set the last profit/loss for the next iteration
        prev_profit_or_loss = current_profit_or_loss

print(total_months)
print(total_profit_or_loss)
print(sum(profit_changes) / len(profit_changes))
