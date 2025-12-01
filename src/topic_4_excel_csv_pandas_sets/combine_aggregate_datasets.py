# %% [markdown]
# # Workflow example for reading and combining CSV files using pandas
# 
# We will read all CSV files from a directory, combine them into a single DataFrame, perform some statistics and then save the combined DataFrame to a new CSV file.
# 
# 

# %%
# we need to load pandas
import pandas as pd
print("Pandas loaded successfully.")

# %%
# get list of all csv files that start with grades_
# we will use Path from pathlib
from pathlib import Path
# let's use rglob
# so change this part to actually pick up on different files as you have them
csv_files = list(Path('.').rglob('grades_*.csv'))
print(f"Found {len(csv_files)} CSV files.")

# %%
# let's load them all as a list of dataframes
dataframes = []
for file in csv_files:
    df = pd.read_csv(file)
    # now we add to a list of separate dataframes
    dataframes.append(df)
print(f"Loaded {len(dataframes)} dataframes.")
# could be 0 could be many many dataframes

# %%
# let's check that dataframes have same columns
# we can use sets for that
first_columns = set(dataframes[0].columns)
all_same = all(set(df.columns) == first_columns for df in dataframes)
print(f"All dataframes have the same columns: {all_same}")
# if not, we cannot combine them directly
if not all_same:
    raise ValueError("Dataframes have different columns and cannot be combined directly.")

# %%
# now we simply concatenate them
combined_df = pd.concat(dataframes, ignore_index=True)
# print information about combined dataframe
print(f"Combined dataframe has {combined_df.shape[0]} rows and {combined_df.shape[1]} columns.")

# %%
# what columns do we have?
print("Columns in combined dataframe:", combined_df.columns.tolist())







# %%
# and let's save the aggregated statistics to a new excel file
# first save to new dataframe
aggregated_stats = combined_df.groupby(['student_name', 'course'])['grade'].describe().reset_index()
# now save to excel
aggregated_stats.to_excel('aggregated_grades_statistics.xlsx', index=False)
print("Aggregated statistics saved to 'aggregated_grades_statistics.xlsx'.")


