import numpy as np
import pandas as pd

print("--- StemMatch Analytics Initialization Check ---")

# Test 1: Vector/Matrix manipulation using NumPy
numerical_array = np.array([10, 20, 30, 40, 50])
mean_value = np.mean(numerical_array)
print(f"NumPy Success! Processing vector array. Calculated Mean: {mean_value}")

# Test 2: Structured Data Tables using Pandas
clinical_data = {
    "Sample_ID": ["STEM-001", "STEM-002"],
    "Expression_Level": [8.45, 9.12]
}
dataframe = pd.DataFrame(clinical_data)
print("\nPandas Success! Structured DataFrame generated:")
print(dataframe)

print("\nEnvironment Status: ALL SYSTEMS GO! Flawless Setup.")
