import json
import pandas as pd
from collections import Counter

# Load cleaned structured dataset
with open("/home/kali/final_project/structured_output_clean.json", "r") as f:
    data = json.load(f)

# Extract MITRE techniques
all_techniques = []

for entry in data:
    techniques = entry.get("MITRE_ATTCK_Techniques", [])
    for t in techniques:
        tech_id = t.get("technique_id")
        tech_name = t.get("technique_name")
        if tech_id and tech_name:
            all_techniques.append(f"{tech_id} - {tech_name}")

# Count occurrences
counter = Counter(all_techniques)

print("\n=== MITRE Technique Frequency ===")
for tech, count in counter.most_common():
    print(f"{tech}: {count}")

# Save to CSV for graphing later
df = pd.DataFrame(counter.items(), columns=["Technique", "Count"])
df.to_csv("/home/kali/final_project/mitre_frequency.csv", index=False)

print("\n[✓] MITRE frequency saved to mitre_frequency.csv")
