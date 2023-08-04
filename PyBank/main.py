import csv

# set data locations
budget_data_path = "PyBank\\Resources\\budget_data.csv"
analysis_data_path = "PyBank\\analysis\\pybank_analysis.txt"

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

# initializers
total_months = 0
total_profit_or_loss = 0
prev_profit_or_loss = 0
profit_changes = []
best_month_increase = ""
best_month_decrease = ""
best_month_increase_value = 0
best_month_decrease_value = 0

# main logic section

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
        total_profit_or_loss += current_profit_or_loss

        # if this isn't the first month, subtract the current profit/loss from the last profit/loss
        # to get the monthly change.  store that in profit changes list.
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

# report our findings

# create an empty file to hold our analysis
create_analysis_file()

# print the content to the analysis file and the console
write_content("Financial Analysis")
write_content("----------------------------")
write_content(f"Total Months: {total_months}")
write_content(f"Total: ${total_profit_or_loss}")
write_content(f"Average Change: ${round(sum(profit_changes) / len(profit_changes), 2)}")
write_content(f"Greatest Increase in Profits: {best_month_increase} (${best_month_increase_value})")
write_content(f"Greatest Decrease in Profits: {best_month_decrease} (${best_month_decrease_value})")
