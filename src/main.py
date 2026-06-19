import numpy as np
import pandas as pd

print("=== StemMatch Analytics Pipeline: Day 7 Data Ingestion ===")

# Path to our data repository vault
data_path = "data/raw_data.csv"

try:
    # Programmatically read and ingest the CSV data
    df = pd.read_csv(data_path)
    print(f"\n[SUCCESS] Ingested spreadsheet file: '{data_path}'")
    
    # Print out structural dimensions
    print(f"Dataset dimensions verified: {df.shape[0]} rows x {df.shape[1]} columns")
    
    # Display the raw parsed dataset table
    print("\n--- Ingested Raw Dataset DataFrame ---")
    print(df)
    
    # Calculate programmatic descriptions of numeric statistics
    print("\n--- Core Matrix Dataset Summary Statistics ---")
    print(df.describe())
    
except FileNotFoundError:
    print(f"\n[ERROR] Pipeline failure: Data file not found at '{data_path}'")



