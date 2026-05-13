"""
Process Mining Discovery Module
-------------------------------
Extracts event logs from the BPI Challenge 2019 dataset, performs data sampling, 
and generates a Directly-Follows Graph (DFG) for process visualization.
"""

import os
import pandas as pd
import pm4py

def main():
    input_file = "BPI_Challenge_2019.xes"
    output_sample = "bpi_2019_sample.csv"
    sample_size = 10000

    print("[INFO] Initializing process discovery module...")

    if not os.path.exists(input_file):
        print(f"[ERROR] Input file '{input_file}' not found in the current directory.")
        return

    # 1. Load Event Log
    print(f"[INFO] Loading event log from '{input_file}'. This may take a few minutes...")
    try:
        df = pm4py.read_xes(input_file)
        print(f"[INFO] Successfully loaded {len(df)} events.")
    except Exception as e:
        print(f"[ERROR] Failed to read XES file: {e}")
        return

    # 2. Data Sampling
    print(f"[INFO] Extracting a sample of {sample_size} events...")
    df_sample = df.head(sample_size).copy()

    # Save sample for future downstream ML tasks
    df_sample.to_csv(output_sample, index=False)
    print(f"[INFO] Sample dataset saved to '{output_sample}'.")

    # 3. Data Formatting for PM4Py
    print("[INFO] Formatting event log attributes...")
    df_sample = pm4py.format_dataframe(
        df_sample, 
        case_id='case:concept:name',        
        activity_key='concept:name', 
        timestamp_key='time:timestamp' 
    )

   # 4. Process Discovery with Filtering 
    print("[INFO] Filtering noise... Keeping the Top 5 most frequent process variants.")
    df_filtered = pm4py.filter_variants_top_k(df_sample, k=5)
    
    print("[INFO] Discovering Directly-Follows Graph (DFG) on filtered data...")
    dfg, start_activities, end_activities = pm4py.discover_dfg(df_filtered)

    # 5. Visualization
    print("[INFO] Rendering process visualization. Please check the pop-up window.")
    try:
        pm4py.view_dfg(dfg, start_activities, end_activities)
    except Exception as e:
        print(f"[ERROR] Graphviz visualization failed: {e}")
        print("[HINT] Ensure Graphviz is installed on your OS and added to the system PATH.")

if __name__ == "__main__":
    main()