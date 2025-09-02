import csv
import pyperclip

# File path to your CSV file
csv_file = 'files/amex.csv'

def getData(description):
    category = ""

    if "PRIVATEPROXY" in description:
        return "VA Private Proxy", "VAs"
    if "PRIVATEPROXY" in description:
        return "VA Private Proxy", "VAs"
    if "Adobe Systems" in description:
        return "Adobe Systems", "Subscriptions"
    if "PADDLE.NET* SMART " in description or "SMARTPRO" in description:
        return "Smart Proxy", "Computing"
    if "LUCKNOW" in description:
        return "Bought Accounts", "Accounts"
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
    if "IMPRESS SOCIA" in description:
        return "Ads Manager", "Advertising"
    if "DocuSign" in description:
        return "DocuSign", "Subscriptions"

    return description, category

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