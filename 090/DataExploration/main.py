#  Created by Simone Margio
#  www.simonemargio.im

import pandas as pd


df = pd.read_csv('salaries_by_college_major.csv')

# Show the first 5 rows of our dataframe
print(f"Show first 5 rows\n{df.head()}\n")

# To see the number of rows and columns
print(f"See the number of rows and columns\n{df.shape}\n")


# We have a row that contains some information regarding the source of the data with blank values for all the other other columns
print(f"Blank values\n{df.tail()}\n")


# Create a new dataframe without the last row and examine the last 5 rows to make sure we removed the last row
clean_df = df.dropna()
print(f"Removed the last row\n {clean_df.tail()}\n")

# Access to a particular column from a data frame
print(f"Access to a particular column from a data frame\n{clean_df['Starting Median Salary']}\n")

# Find the highest starting salary
print(f"Highest salary\n{clean_df['Starting Median Salary'].max()}\n")

# Index for the row with the largest value
print(f"Index for the row with the largest value (43)\n{clean_df['Starting Median Salary'].idxmax()}\n")

# Name of the major that corresponds to that particular row
print(f"\n{clean_df['Undergraduate Major'].loc[43]}\n")

# The Highest Mid-Career Salary
print(f"\nHighest Mid-Career Salary: {clean_df['Mid-Career Median Salary'].max()}\n")
print(f"\nIndex for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}\n")
clean_df['Undergraduate Major'][8]

# Lowest Starting and Mid-Career Salary
print(f"\nLowest Starting and Mid-Career Salary: {clean_df['Starting Median Salary'].min()}\n")


# Majors with the Highest Potential
highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print(f"Majors with the Highest Potential\n{highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()}\n")