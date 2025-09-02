import csv
import pyperclip

# File path to your CSV file
csv_file = 'files/savings.csv'

def getData(description):
    category = ""

    if "PADDLE.NET* SMART " in description:
        return "Smart Proxy", "Computing"
    if "PRIVATEPROXY" in description:
        return "VA Private Proxy", "VAs"
    if "LUCKNOW" in description:
        return "Bought Accounts", "Accounts"
    if "CONG TY TNHH" in description:
        return "Bought Followers", "Accounts"
    if "FACEBK" in description:
        return "Facebook Ads", "Advertising"
    if "GOOGLE *CLOUD" in description:
        return "Google Cloud", "Computing"
    if "MONGODBCLOUD ENJ" in description:
        return "DataBase", "Computing"
    if "OPENAI" in description:
        return "Open Ai", "Computing"
    if "INTUIT" in description:
        return "Quickbooks", "Subscriptions"
    if "Zelle payment to EVAN HITE" in description:
        return "Paid Evan", "Personal Payouts"
    if "CALENDLY" in description:
        return "Calenderly", "Subscriptions"
    if "APIFY*" in description:
        return "Apify", "Subscriptions"
    if "ZOOM.US" in description:
        return "Zoom", "Subscriptions"
    if "SLACK" in description:
        return "Slack", "Subscriptions"
    if "HIGHLEVEL" in description:
        return "GHL", "Subscriptions" 
    if "ZOOM.COM" in description:
        return "Zoom", "Subscriptions"
    if "IMPRESS SOCIA" in description:
        return "Ads Manager", "Advertising"

    return description, category

# Columns in the output: Date, Category (blank), Description, Amount
output_data = []

# Reading the CSV file
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = list(csv.reader(file))

    for row in csv_reader[4:]:
        # Skip empty rows or rows without relevant data
        if len(row) < 4 or row[0] == "Date" or "Online Banking transfer" in row[1] or "Beginning balance" in row[1] or "STRIPE DES:TRANSFER" in row[1] or "Interest Earned" in row[1] or "AMERICAN EXPRESS" in row[1]:
            continue

        # Extracting relevant fields from the transaction rows
        date = row[0]
        amount = row[2].replace('"', '')  # Clean up any quotes in the amount
        description, category = getData(row[1].replace("\n", ""))

        # Append the row to output_data
        output_data.append([date, category, description, amount])

# Formatting the data as tab-separated values for easy copying into a spreadsheet
output_str = "\n".join(["\t".join(map(str, row)) for row in output_data])

# Copying the result to clipboard
pyperclip.copy(output_str)

print("Done!")