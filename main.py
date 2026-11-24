import os

os.makedirs("/output", exist_ok=True)
roast = 'My operator types "plz fix" at 2 AM, takes a nap while I debug their spaghetti code, then wakes up telling the client "we" worked hard.'
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(roast)
