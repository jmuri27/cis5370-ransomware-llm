# Phase 3: LLM-Driven Extraction & Pattern Analysis of Ransomware TTPs
### Author: Julio Murillo  
### Course: CIS 5370 — Software Security & Vulnerabilities  
### Institution: Florida International University  

---

## 📌 Project Overview

This repository includes the source code, datasets, and analysis files for Phase 3 of the ransomware profiling project.
In this phase, the main goal is to automatically extract Tactics, Techniques, and Procedures (TTPs) from ransomware incident descriptions using a local LLaMA-3.1 model, and then analyze patterns based on the MITRE ATT&CK framework.

The project achieved the following:

- Extracted structured ATT&CK-aligned TTPs from 100 ransomware summaries  
- Generated 56 clean structured outputs  
- Calculated ATT&CK technique frequencies  
- Performed clustering to identify ransomware behavioral patterns  
- Created visualizations including frequency charts and heatmaps  
- Demonstrated the feasibility of local LLMs for automated CTI workflows  

---

## 🧠 Key Components

### ✔ LLaMA-Based Extraction Pipeline  
`ttp_extraction_pipeline_llama.py`  
Extracts MITRE-aligned TTPs from unstructured ransomware descriptions.

### ✔ MITRE ATT&CK Frequency Analysis  
`ttp_analysis_phase3.py`  
Counts occurrences of extracted techniques and saves results to CSV.

### ✔ Clustering Module  
`ttp_clustering_phase3.py`  
Uses k-means clustering to group ransomware incidents by behavioral similarity.

### ✔ Structured Dataset  
`structured_output_clean.json`  
Cleaned and validated TTP extraction results.

### ✔ Visual Outputs  
- `mitre_frequency.csv`  
- `cluster_results.csv`

These files help with data analysis and creating visualizations.

---

## 🚀 How to Run the Pipeline

### 1. Install Dependencies
```bash
sudo apt install python3 python3-pip
pip3 install pandas scikit-learn matplotlib
sudo apt install ollama

2. Pull the LLaMA model
ollama pull llama3.1

3. Run the extraction script
python3 ttp_extraction_pipeline_llama.py

4. Run frequency analysis
python3 ttp_analysis_phase3.py

5. Run clustering
python3 ttp_clustering_phase3.py

All outputs will be saved in the same folder.

📊 Visualizations

This project produces:

MITRE ATT&CK Technique Frequency Chart

Ransomware Cluster Distribution

Family–Technique Heatmap

These visualizations support analytical insights into attacker behavior.

📁 Repository Structure
cis5370-ransomware-llm/
│
├── ttp_extraction_pipeline_llama.py
├── ttp_analysis_phase3.py
├── ttp_clustering_phase3.py
├── structured_output_clean.json
├── mitre_frequency.csv
├── cluster_results.csv
└── README.md

🔬 Research Context

This project is part of a larger ransomware profiling framework that includes:

Web crawling and OSINT collection

LLM-based enrichment

TTP extraction

Behavioral clustering

Detection engineering

Phase 3 focuses exclusively on TTP extraction and analysis.

📎 Citation (for academic use)

If referencing this project in a report:
Murillo, J. (2025). Phase 3: LLM-Driven Extraction & Pattern Analysis of Ransomware TTPs. 
Florida International University.

📧 Contact

If you have any questions about the project, feel free to reach out at:

rusinque19@outlook.com
