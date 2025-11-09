# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 20:07:34 2025

@author: El-Wattaneya
"""


# Module 10 Assignment


____________________________________________________________
# Importing Libraries
import pandas as pd

# Loading Dataset
df = pd.read_csv(r"C:\Users\El-Wattaneya\Desktop\Assignment 10\small_health_dataset.csv")

# Printing the dataset
df

_____________________________________________________________
# 1. MELT
# Melt converts wide data (many columns) into long data (few columns)
# I will melt columns related to procedures, medications, and visits.

melted = pd.melt(
    df,
    id_vars=["Patient_ID", "Gender", "Diagnosis"],
    value_vars=["Num_Lab_Procedures", "Num_Medications", "Num_Visits"],
    var_name="Measure",
    value_name="Value"
)

print(" Melt Example:")
print(melted, "\n")

_______________________________________________________________
# 2. PIVOT

# Since Pivot does the opposite of melt: I will use it to spread the 'Measure' column back into separate columns.

pivoted = melted.pivot(
    index=["Patient_ID", "Gender", "Diagnosis"],
    columns="Measure",
    values="Value"
)

print("Pivot Example:")
print(pivoted, "\n")
# Now we will have separate columns for "Num_Lab_Procedures", "Num_Medications", "Num_Visits"


_________________________________________________________________
# 3. AGGREGATION

# for that I will find average, minimum and maximum number for the lab procedures, medications, and visits by diagnosis.

agg = df.groupby("Diagnosis")[["Num_Lab_Procedures", "Num_Medications", "Num_Visits"]].agg(["mean", "max", "min"])
print(" Aggregation Example:")
print(agg, "\n")


________________________________________________________________
# 4. ITERATION

# I will Iterate through Patient ID, Gender, Diagnosis, and Num_lab _Procedure rows using iterrows() and print a custom message for each patient.

print(" Iteration Example:")
for index, row in df.iterrows():
    print(f"Patient {row['Patient_ID']} ({row['Gender']}) was diagnosed with {row['Diagnosis']} and had {row['Num_Lab_Procedures']} lab procedures.")
print("\n")


_______________________________________________________________
# 5. GROUPBY

# I will group data by gender and calculate average hospital saty and average number of medication

grouped = df.groupby("Gender")[["Hospital_Stay_Days", "Num_Medications"]].mean()
print(" Groupby Example:")
print(grouped, "\n")


