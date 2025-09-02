def parse_data(description):
    category = "Uncategorized"

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
    if any(sub in description for sub in ["GOOGLE *CLOUD", "GOOGLE*CLOUD"]):
        return "Google Cloud", "Computing"
    if "MONGODBCLOUD ENJ" in description:
        return "DataBase", "Computing"
    if "OPENAI" in description:
        return "Open Ai", "Computing"
    if "MULTILOGIN.COM" in description:
        return "Multilogin", "Computing"
    if "INTUIT" in description:
        return "Quickbooks", "Subscriptions"
    if "Zelle payment to EVAN HITE" in description:
        return "Monthly Salary", "Paid Evan"
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
    if "Adobe Systems" in description:
        return "Adobe Systems", "Subscriptions"
    if "DocuSign" in description:
        return "DocuSign", "Subscriptions"
    if "APPOTAP*CONG" in description:
        return "Bought Followers", "Accounts"

        

    return description, category