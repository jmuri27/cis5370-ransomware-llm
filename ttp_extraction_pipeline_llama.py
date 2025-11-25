"""
TTP Extraction Pipeline using Local LLaMA Model
Author: Julio Murillo
Course: CIS 5370 – Final Project
Description:
    This script processes a real ransomware incident dataset and performs
    automated Threat Tactic, Technique, and Procedure (TTP) extraction using
    a locally running LLaMA model via the Ollama framework.

    The script:
        • Loads the Kaggle ransomware dataset (2020–2024)
        • Extracts short textual descriptions for each incident
        • Sends each description to an LLM with a structured extraction prompt
        • Receives JSON containing:
            - ransomware_family
            - victim details
            - MITRE ATT&CK techniques
            - initial access vectors
            - persistence mechanisms
            - ransom demands
            - exfiltration methods
        • Saves the structured results to a JSON file for later trend analysis,
          clustering, and visualization in Phase 3 of the project.

    This script forms the core data processing pipeline for the academic analysis.
"""

import pandas as pd
import json
import subprocess
import re


# -----------------------------
# CONFIGURATION
# -----------------------------

MODEL = "llama3.1"

SYSTEM_PROMPT = """
You are a cybersecurity threat intelligence assistant specializing in ransomware analysis.

Your task is to extract structured fields from a short incident summary.
If information is not explicitly stated, you may infer common ransomware behaviors,
but you MUST mark inferred data with "inferred": true.

Return ONLY valid JSON with the following fields:

- ransomware_family
- victim_name
- victim_industry
- country
- attack_date
- vulnerability_used
- initial_access_method
- exfiltration_tool
- persistence_mechanism
- ransom_amount
- data_leak

For MITRE ATT&CK, return a LIST of objects:
"MITRE_ATTCK_Techniques": [
    {
        "tactic_id": "TA0001",
        "tactic_name": "Initial Access",
        "technique_id": "T1566",
        "technique_name": "Phishing",
        "inferred": false
    }
]

If no MITRE techniques are described or inferable, return an empty list.

If ANYTHING is unknown: use null.

Strictly return ONLY JSON.
"""

DATASET_PATH = "/home/kali/final_project/data/global_ransomware_incidents_2020_2024.csv"
OUTPUT_JSON = "structured_output.json"


# ---------------------------------------------
# FUNCTION: Call LLaMA via the Ollama framework
# ---------------------------------------------
def call_llama(prompt_text):
    """
    Sends a prompt to the local LLaMA model through the Ollama CLI.
    """
    full_prompt = SYSTEM_PROMPT + "\n" + prompt_text
    cmd = ["ollama", "run", MODEL]

    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = process.communicate(full_prompt.encode())[0].decode()

    return output


# -----------------------------
# MAIN EXTRACTION LOOP
# -----------------------------
def main():

    # Load dataset
    df = pd.read_csv(DATASET_PATH)

    # TEMPORARY LIMIT FOR TESTING (remove later for full extraction)
   # df = df.head(5)

    results = []

    for idx, row in df.iterrows():
        print(f"[+] Processing entry {idx+1}/{len(df)}...")

        text_summary = row["Brief Description"]
        prompt = f"Extract structured cybersecurity TTP data from this summary:\n{text_summary}"

        response = call_llama(prompt)

        # -----------------------------
        # CLEAN AND PARSE JSON OUTPUT
        # -----------------------------
        try:
            # 1. Extract JSON inside ``` ``` blocks if present
            match = re.search(r"```(?:json)?(.*?)```", response, re.DOTALL)
            if match:
                cleaned = match.group(1).strip()
            else:
                # 2. Fallback: find first JSON object { ... }
                json_match = re.search(r"\{.*\}", response, re.DOTALL)
                if not json_match:
                    raise ValueError("No JSON found in response.")
                cleaned = json_match.group(0).strip()

            # 3. Parse cleaned JSON
            parsed_json = json.loads(cleaned)
            results.append(parsed_json)

        except Exception as e:
            results.append({
                "error": "Invalid JSON format",
                "raw_output": response,
                "exception": str(e)
            })

    # Save results
    with open(OUTPUT_JSON, "w") as f:
        json.dump(results, f, indent=4)

    print("\n[✓] Extraction completed successfully.")
    print(f"[✓] Output saved to: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
