# -*- coding: utf-8 -*- 
"""
Created on Sat Nov 22 14:32:13 2025

@author: El-Wattaneya
"""

#%% -------------------------------------------------------------------------
#Importing Libraries
#----------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt     


#%% -------------------------------------------------------------------------
# Loading COVID-19 U.S. time-series dataset
#----------------------------------------------------------------------------


url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
covid_df = pd.read_csv(url, index_col=0)

# Displaying the dataframe for inspection
covid_df


#%% -------------------------------------------------------------------------
# Visualization 1: 
#----------------------------------------------------------------------------

from datetime import datetime       # To convert string dates to datetime objects for plotting

# Only keep date columns (skip metadata columns such as FIPS, Admin2, Province_State, etc.)
date_cols = covid_df.columns[11:]

# Helper function: converts "MM/DD/YY" strings to datetime objects
# Necessary because matplotlib handles datetime objects better than strings
def convert_dates(cols):
    return [datetime.strptime(c, "%m/%d/%y") for c in cols]

# Applying conversion function to get a list of datetime objects
dates = convert_dates(date_cols)

# Filtering data for Utah only
utah = covid_df[covid_df["Province_State"] == "Utah"]

# Creating a new figure of specified size (width=12 inches, height=6 inches)
plt.figure(figsize=(12,6))

# Plotting each county in light gray
for _, row in utah.iterrows():
    plt.plot(dates, row[date_cols], color='lightgray', linewidth=1)

# Highlighting Salt Lake County with a thick blue line
slc = utah[utah["Admin2"] == "Salt Lake"].iloc[0]
plt.plot(dates, slc[date_cols], color='blue', linewidth=2.5, label="Salt Lake County")

# Adding title and axis labels
plt.title("COVID-19 Cases Over Time in Utah Counties")
plt.xlabel("Date")
plt.ylabel("Cumulative Cases")

# Adding legend to distinguish Salt Lake County
plt.legend()

# Adjusting layout to prevent label/legend overlap
plt.tight_layout()

# Showing the created plot
plt.show()


#%% -------------------------------------------------------------------------
# Visualization 2: 
#----------------------------------------------------------------------------


# .max(axis=1) finds the highest cumulative value per row
# .idxmax() returns the index of the row with the overall maximum
utah_max = utah.loc[utah[date_cols].max(axis=1).idxmax()]

# Repeating  for Florida
florida = covid_df[covid_df["Province_State"] == "Florida"]
fl_max = florida.loc[florida[date_cols].max(axis=1).idxmax()]

# Creating figure
plt.figure(figsize=(12,6))

# Plotting Utah highest-case county
plt.plot(
    dates, utah_max[date_cols],
    label=f"Utah – {utah_max['Admin2']} County",
    linewidth=2
)

# Plotting Florida highest-case county
plt.plot(
    dates, fl_max[date_cols],
    label=f"Florida – {fl_max['Admin2']} County",
    linewidth=2
)

# Adding Titles and axis labels
plt.title("Comparison: Highest Case Counties (Utah vs Florida)")
plt.xlabel("Date")
plt.ylabel("Cumulative Cases")

# Adding legend
plt.legend()

#Adjusting Layout
plt.tight_layout()

#Showing the plot
plt.show()


#%% -------------------------------------------------------------------------
# Visualization 3:
#----------------------------------------------------------------------------

# Extracting cumulative series for Salt Lake County
series = slc[date_cols]

# Computing daily new cases by differencing cumulative counts
# .diff() subtracting previous day's value and filling NaN for first value with 0
daily_new = series.diff().fillna(0)

# Creating figure with one axis
fig, ax1 = plt.subplots(figsize=(12,6))

# Line plot: cumulative cases and labeling the y axis
ax1.plot(dates, series, color="green", label="Cumulative Cases")
ax1.set_ylabel("Cumulative Cases", color="green")  

# Bar plot: daily new cases on a secondary y-axis
ax2 = ax1.twinx()
ax2.bar(dates, daily_new, alpha=0.4, label="Daily New Cases")
ax2.set_ylabel("Daily New Cases")

# Adding title
plt.title("Salt Lake County: Cumulative Cases vs Daily New Cases")

# Auto-format x-axis dates to avoid overlapping
fig.autofmt_xdate()

# Getting legend handles from both axes
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()

# Placing legend fully outside the plot on the right
fig.legend(
    handles1 + handles2,
    labels1 + labels2,
    loc="center right",
    bbox_to_anchor=(1.15, 0.5)
)

#Adjusting layout
plt.tight_layout()

#showing the plot
plt.show()


#%% -------------------------------------------------------------------------
# Visualization 4: Delaware stacked bar chart
# Selected Delaware as it has a small number of counties for readability
#----------------------------------------------------------------------------

state = "Delaware"
de = covid_df[covid_df["Province_State"] == state]

# Getting final cumulative cases (last date column) for each county
final_cases = de[date_cols[-1]]

# sorting counties largest → smallest for consistent stacked order
de_sorted = de.assign(Final=final_cases).sort_values("Final", ascending=False)

# Creating figure
plt.figure(figsize=(8,6))

bottom = 0  # Tracking cumulative height for stacking
handles = [] # Storing bars for legend
labels = []  # Storing county names

# Loop over counties and create stacked bars
for _, row in de_sorted.iterrows():
    bar = plt.bar(state, row["Final"], bottom=bottom, label=row["Admin2"])
    handles.append(bar)
    labels.append(row["Admin2"])
    bottom += row["Final"]  # Increment bottom for next bar

# adding Titles and labels
plt.title("County Contributions to Total COVID-19 Cases in Delaware")
plt.ylabel("Total Cases")

# Placing legend outside plot to avoid overlap
plt.legend(handles, labels, bbox_to_anchor=(1.05, 1), loc='upper left')

#Adjusting layout
plt.tight_layout()

#showing plot
plt.show()


#%% -------------------------------------------------------------------------
# Extra Credit: 
#----------------------------------------------------------------------------

#Importing Seaborn
import seaborn as sns  

# Computing total cumulative cases for each state (used to order the states)
state_totals = covid_df.groupby("Province_State")[date_cols[-1]].sum().sort_values(ascending=False)
ordered_states = state_totals.index  # Ordering states by total cases

# Convert wide-form data (columns=dates) to long-form for seaborn
# Each row = one county on one date
box_df = covid_df[["Province_State"] + date_cols.tolist()]
box_df_long = box_df.melt(
    id_vars="Province_State",   # Keep state as identifier
    var_name="Date",            # New column with dates
    value_name="Cases"          # New column with cumulative cases
)

# Creating figure for boxplot
plt.figure(figsize=(28,20))

# Boxplot showing distribution of county-level cases per state
sns.boxplot(
    data=box_df_long,
    x="Province_State",
    y="Cases",
    order=ordered_states
)

plt.xticks(rotation=90)  # Rotate x-axis labels
plt.title("Extra Credit: Distribution of County-Level Cases by State")

#Adjusting layout
plt.tight_layout()

#showing plot
plt.show()

#_____________________________________________________________
# Extra Credit: Violin plot + log scale (more visually appealing)
#----------------------------------------------------------------------------

plt.figure(figsize=(28,20))

# Drop rows with missing cases
box_df_long_clean = box_df_long.dropna(subset=["Cases"])

# Violin plot shows distribution density per state
sns.violinplot(
    data=box_df_long_clean,
    x="Province_State",
    y="Cases",
    order=ordered_states,
    inner=None,   # Remove inner bars for clarity
    scale="width" # Keep width consistent across states
)

# Using log scale for y-axis to handle skewed case numbers
plt.yscale("log")

# Rotating x-axis labels for readability
plt.xticks(rotation=90)

# Adding descriptive title
plt.title("Extra Credit: County-Level Distribution of COVID-19 Cases by State (Log Scale, Violin Plot)")

#Adjusting layout
plt.tight_layout()

#showing plot
plt.show()

