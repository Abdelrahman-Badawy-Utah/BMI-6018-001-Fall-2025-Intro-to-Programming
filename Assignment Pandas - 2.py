# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 22:04:20 2025

@author: El-Wattaneya
"""

import pandas as pd
import numpy as np

# Question 1 

# Input data
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# 1. Calculating the difference between the series (p - q)
difference = p - q

# 2. Squaring the differences
squared_diff = difference ** 2

# 3. Suming all the squared differences
sum_squared_diff = np.sum(squared_diff)

# 4. Taking the square root of the sum
euclidean_dist = np.sqrt(sum_squared_diff)

print(f"p Series:\n{p}")
print(f"q Series:\n{q}")
print(f"Euclidean Distance: {euclidean_dist}\n")

##### more simple soultion would be importing math:

import math

distance = math.sqrt(((p - q) ** 2).sum())
print(distance)
    


#__________________________________________________________________
# Question 2 


# Input data
df_q2 = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
print(f"Original DataFrame (Q2):\n{df_q2}")

# Getting the list of columns
cols = list(df_q2.columns)

# Finding the indices (positions) of columns 'a' and 'c'
a_index = cols.index('a')
c_index = cols.index('c')

# Swaping the column names in the list
cols[a_index], cols[c_index] = cols[c_index], cols[a_index]

# Re-indexing the DataFrame with the new column order
df_q2 = df_q2[cols]

print(f"\nDataFrame with 'a' and 'c' swapped:\n{df_q2}\n")

##### more simple solution but less robust would be:
# New column order
cols = ['c', 'b', 'a', 'd', 'e']

# Reindexing the dataframe
df_new = df_q2[cols]
print(df_new)



#_______________________________________________________________
# Question 3 

def swap_columns(df_in, col1, col2):

    # Creating a copy of the column list
    cols = list(df_in.columns)

    # Geting the index (position) of each column
    try:
        idx1 = cols.index(col1)
        idx2 = cols.index(col2)
    except ValueError as e:
        print(f"Error: Column not found. {e}")
        return df_in # Returning original DataFrame if a column is missing

    # Swaping the items in the list
    cols[idx1], cols[idx2] = cols[idx2], cols[idx1]

    # Returning the DataFrame re-indexed with the new column order
    return df_in[cols]

# Input data
df_q3 = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
print(f"Original DataFrame (Q3):\n{df_q3}")

# Using the generic function to swap 'a' and 'c'
df_q3_swapped = swap_columns(df_q3, 'a', 'c')
print(f"\nDataFrame after swapping 'a' and 'c' with function:\n{df_q3_swapped}\n")

# Example of swapping 'b' and 'e'
df_q3_swapped_be = swap_columns(df_q3, 'b', 'e')
print(f"DataFrame after swapping 'b' and 'e' with function:\n{df_q3_swapped_be}\n")





#_________________________________________________________________
#Question 4 


# Creating the DataFrame with random numbers raised to the power of 10
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])

# Printing the original DataFrame
print("Original DataFrame:")
print(df)

# Step 1: Rounding the numbers to 4 decimal places
# This also suppresses scientific notation for small numbers
df['random'] = df['random'].round(4)

# Step 2: Printing the formatted DataFrame
print("\nFormatted DataFrame (4 decimals, no scientific notation):")
print(df)



#_______________________________________________________________________
#  Question 5

# Creating the DataFrame
df = pd.DataFrame(np.random.randint(1, 100, 40).reshape(10, -1), 
                  columns=list('pqrs'), 
                  index=list('abcdefghij'))

print("Original DataFrame:\n", df)


# Step 1: Defining a function to compute Euclidean distance between two rows
def euclidean_distance(row1, row2):
    return np.sqrt(np.sum((row1 - row2) ** 2))

# Step 2: Initializing lists to store nearest row and distance
nearest_rows = []
distances = []

# Step 3: Looping through each row to find its nearest row
for idx1, row1 in df.iterrows():
    min_dist = float('inf')   # start with a very large number
    nearest_idx = None
    for idx2, row2 in df.iterrows():
        if idx1 == idx2:
            continue  # skip the same row
        dist = euclidean_distance(row1, row2)
        if dist < min_dist:
            min_dist = dist
            nearest_idx = idx2
    nearest_rows.append(nearest_idx)
    distances.append(min_dist)

# Step 4: Adding the new columns to the DataFrame
df['nearest_row'] = nearest_rows
df['dist'] = distances

# Step 5: Printing the final DataFrame
print("\nDataFrame with nearest row and distance:\n", df)




#________________________________________________________________________
# Question 6 
# Input data
data = {'A': [45, 37, 0, 42, 50],
        'B': [38, 31, 1, 26, 90],
        'C': [10, 15, -10, 17, 100],
        'D': [60, 99, 15, 23, 56],
        'E': [76, 98, -0.03, 78, 90]
        }

# Creating a DataFrame
df = pd.DataFrame(data)

# Step 1: Computing the correlation matrix
correlation_matrix = df.corr()

# Step 2: Printing the correlation matrix
print("Correlation matrix:")
print(correlation_matrix)
