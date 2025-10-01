import csv
import re
import pyperclip
from datetime import datetime

csv_file = 'files/stripe.csv'

rows = []
with open(csv_file, mode='r', newline='', encoding='utf-8') as f:
    r = csv.DictReader(f)
    for row in r:
        dt = datetime.strptime(row["Created date (UTC)"], "%Y-%m-%d %H:%M:%S")
        desc = row.get("Description", "") or ""
        # Normalize CRLF or CR to spaces, collapse runs of whitespace
        desc = re.sub(r"\s+", " ", desc.replace("\r", "\n")).strip()
        if not desc:
            desc = row.get("Statement Descriptor", "") or ""
        rows.append([dt, desc, row["Amount"], row["Fee"]])

rows.sort(key=lambda x: x[0])

out = []
for dt, desc, amt, fee in rows:
    out.append([dt.strftime("%m/%d/%Y"), desc, amt, fee])

output_str = "\n".join("\t".join(map(str, r)) for r in out)
pyperclip.copy(output_str)
print("Done!")
