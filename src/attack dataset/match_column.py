import pandas as pd
import numpy as np

# Read the original CSV file and assign column names
df = pd.read_csv('reordered_features_no_empty_rows.csv', names=[
    "Destination Port", "Flow Duration", "Total Length of Fwd Packets", 
    "FIN Flag Count", "SYN Flag Count", "RST Flag Count"
])

# Convert columns to numeric, coerce errors to NaN for invalid entries
df["Flow Duration"] = pd.to_numeric(df["Flow Duration"], errors='coerce')
df["Destination Port"] = pd.to_numeric(df["Destination Port"], errors='coerce')
df["Total Length of Fwd Packets"] = pd.to_numeric(df["Total Length of Fwd Packets"], errors='coerce')
df["FIN Flag Count"] = pd.to_numeric(df["FIN Flag Count"], errors='coerce')
df["SYN Flag Count"] = pd.to_numeric(df["SYN Flag Count"], errors='coerce')
df["RST Flag Count"] = pd.to_numeric(df["RST Flag Count"], errors='coerce')

# Fill NaN values with 0 (or any appropriate value based on your requirements)
df = df.fillna(0)

# Convert Flow Duration to microseconds (assuming original data is in seconds)
df["Flow Duration"] = (df["Flow Duration"] * 1e6).astype(int)  # Convert to microseconds and round to integer

# Ensure all columns match the unit and data format of the 2017 dataset
df["Destination Port"] = df["Destination Port"].astype(int)
df["Total Length of Fwd Packets"] = df["Total Length of Fwd Packets"].astype(int)
df["FIN Flag Count"] = df["FIN Flag Count"].astype(int)
df["SYN Flag Count"] = df["SYN Flag Count"].astype(int)
df["RST Flag Count"] = df["RST Flag Count"].astype(int)

# Save to a new CSV file
df.to_csv('reordered_features_2017_format.csv', index=False)

print("CSV file generated successfully with units and format matching the 2017 dataset.")
