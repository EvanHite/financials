import csv
import pyperclip
from parse import getData

# File path to your CSV file
csv_file = 'files/amex.csv'

# Columns in the output: Date, Category (blank), Description, Amount
output_data = []

# Reading the CSV file
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = list(csv.reader(file))

    for row in csv_reader[1:]:
        if len(row) < 4 or row[0] == "Date" or "-" in row[5]:
            continue
        # Extracting relevant fields from the transaction rows
        date = row[0]
        amount = row[5].replace('"', '')  # Clean up any quotes in the amount
        description, category = getData(row[2].replace("\n", ""))
        cardMember = row[3].replace('"', '')
        # Append the row to output_data
        output_data.append([date, category, description, "-"+amount,cardMember])

# Formatting the data as tab-separated values for easy copying into a spreadsheet
output_str = "\n".join(["\t".join(map(str, row)) for row in output_data])

# Copying the result to clipboard
pyperclip.copy(output_str)

print("Done!")