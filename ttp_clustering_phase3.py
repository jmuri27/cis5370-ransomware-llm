import json
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

# Load dataset
with open("/home/kali/final_project/structured_output_clean.json", "r") as f:
    data = json.load(f)

# Convert MITRE techniques to strings
rows = []
for entry in data:
    family = entry.get("ransomware_family", "Unknown")
    techniques = entry.get("MITRE_ATTCK_Techniques", [])

    technique_strings = []
    for t in techniques:
        tech_id = t.get("technique_id")
        tech_name = t.get("technique_name")
        if tech_id and tech_name:
            technique_strings.append(f"{tech_id}_{tech_name}")

    rows.append({
        "family": family,
        "techniques": " ".join(technique_strings)
    })

df = pd.DataFrame(rows)

# Vectorize technique text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["techniques"])

# Run k-means clustering
kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
df["cluster"] = kmeans.labels_

print(df.head())

# Save results
df.to_csv("/home/kali/final_project/cluster_results.csv", index=False)
print("\n[✓] Clustering results saved to cluster_results.csv")
