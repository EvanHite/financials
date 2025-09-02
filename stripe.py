import csv
import pyperclip
from datetime import datetime

# File path to your CSV file
csv_file = 'files/stripe.csv'

# Columns in the output: Date, Category (blank), Amount, Fee
data_rows = []

# Reading the CSV file
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Extracting required fields
        # Parse date and format it as MM/DD/YYYY
        date_time_str = row["Created date (UTC)"]
        date_obj = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")  # Convert to datetime object
        
        category = row["Description"].replace("\n","")
        amount = row["Amount"]
        fee = row["Fee"]
        
        # Append the row to data_rows (keeping date_obj for sorting)
        data_rows.append([date_obj, category, amount, fee])

# Sort the rows by the date (ascending order, oldest to newest)
data_rows.sort(key=lambda x: x[0])

# Prepare output data with formatted dates
output_data = []  

for row in data_rows:
    date = row[0].strftime("%m/%d/%Y")  # Format the date as MM/DD/YYYY
    output_data.append([date, row[1], row[2], row[3]])

# Formatting the data as tab-separated values for easy copying into a spreadsheet
output_str = "\n".join(["\t".join(map(str, row)) for row in output_data])

# Copying the result to clipboard
pyperclip.copy(output_str)

print("Done!")
