def getData(description):
    category = ""

    if "PADDLE.NET* SMART " in description or "SMARTPRO" in description:
        return "Smart Proxy", "Computing"
    if "PRIVATEPROXY" in description:
        return "VA Private Proxy", "VAs"
    if "LUCKNOW" in description:
        return "Bought Accounts", "Accounts"
    if "CONG TY TNHH" in description:
        return "Bought Followers", "Accounts"
    if "FACEBK" in description:
        return "Facebook Ads", "Advertising"
    if "GOOGLE *CLOUD" in description or "GOOGLE*CLOUD" in description:
        return "Google Cloud", "Computing"
    if "MONGODBCLOUD ENJ" in description:
        return "DataBase", "Computing"
    if "OPENAI" in description:
        return "Open Ai", "Computing"
    if "INTUIT" in description:
        return "Quickbooks", "Subscriptions"
    if "ZELLE PAYMENT TO EVAN HITE" in description:
        return "Paid Evan", "Personal Payouts"
    if "CALENDLY" in description:
        return "Calendly", "Subscriptions"
    if "APIFY*" in description:
        return "Apify", "Subscriptions"
    if "ZOOM.US" in description or "ZOOM.COM" in description:
        return "Zoom", "Subscriptions"
    if "SLACK" in description:
        return "Slack", "Subscriptions"
    if "HIGHLEVEL" in description:
        return "GHL", "Subscriptions"
    if "IMPRESS SOCIA" in description:
        return "Ads Manager", "Advertising"
    if "ADOBE SYSTEMS" in description:
        return "Adobe Systems", "Subscriptions"
    if "DOCUSIGN" in description:
        return "DocuSign", "Subscriptions"
    if "NAME-CHEAP.COM" in description or "NAMECHEAP" in description:
        return "NameCheap", "Subscriptions"

    return description, category