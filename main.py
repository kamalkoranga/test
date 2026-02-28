import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "https://startuputtarakhand.uk.gov.in/recognised_startups?page="
all_data = []

for page in range(1, 30):  # increase if needed
    print(f"Scraping page {page}...")
    url = f"{base_url}{page}"
    
    r = requests.get(url)
    if r.status_code != 200:
        break

    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find("table")

    if not table:
        continue

    # Extract headers (column names)
    headers = []
    header_row = table.find("tr")
    for th in header_row.find_all(["th", "td"]):
        headers.append(th.text.strip())

    # Extract rows
    rows = table.find_all("tr")[1:]  # skip header

    for row in rows:
        cols = row.find_all("td")
        if len(cols) == len(headers):
            row_data = {}
            for i in range(len(headers)):
                row_data[headers[i]] = cols[i].text.strip()

            all_data.append(row_data)

    time.sleep(1)  # be polite to server

# Convert to DataFrame
df = pd.DataFrame(all_data)

# ---------------------------
# 🎯 FILTER POTENTIAL SPONSORS
# ---------------------------

# Keywords that match companies likely to sponsor tech hackathons
sponsor_keywords = [
    "Technology", "IT", "Software", "AI", "Fintech",
    "EdTech", "Cyber", "Data", "Innovation", "Digital",
    "Robotics", "Blockchain", "Cloud"
]

# Filter based on Sector / Industry columns
df_filtered = df[
    df.apply(lambda row: any(
        keyword.lower() in str(row).lower()
        for keyword in sponsor_keywords
    ), axis=1)
]

# Save both files
df.to_excel("all_recognised_startups.xlsx", index=False)
df_filtered.to_excel("potential_hackathon_sponsors.xlsx", index=False)

print("Done ✅")
print(f"Total startups scraped: {len(df)}")
print(f"Potential sponsors found: {len(df_filtered)}")



# asdasfjnakfn
sfkjsdlfsdkfj
asdjalksjdkasf


##dsfsdfkjsdlfj
changes 3