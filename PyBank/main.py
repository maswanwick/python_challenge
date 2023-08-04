import csv

# set data location
budget_data_path = "PyBank\\Resources\\budget_data.csv"

# initializers
total_months = 0
total_profit_or_loss = 0
prev_profit_or_loss = 0
profit_changes = []
best_month_increase = ""
best_month_decrease = ""
best_month_increase_value = 0
best_month_decrease_value = 0

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
        # to get the monthly change.  Store that in profit changes list.
        # then test to see if the change is outside the current high or low marks.  if it is, 
        # store that value along with the month
        if (total_months > 1):
            current_change = current_profit_or_loss - prev_profit_or_loss
            profit_changes.append(current_change)
        
            if (current_change > best_month_increase_value):
                best_month_increase_value = current_change
                best_month_increase = budget_data_record[header.index("Date")]
            elif (current_change < best_month_decrease_value):
                best_month_decrease_value = current_change
                best_month_decrease = budget_data_record[header.index("Date")]
            
        # set the last profit/loss for the next iteration
        prev_profit_or_loss = current_profit_or_loss

print(total_months)
print(total_profit_or_loss)
print(sum(profit_changes) / len(profit_changes))
print(f"Increase: {best_month_increase} {best_month_increase_value}")
print(f"Decrease: {best_month_decrease} {best_month_decrease_value}")

