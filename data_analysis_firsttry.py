"""
# this is a funtion to unit excel and find difficulty.
# 这是一个整合excel找到diffculty的功能
import pandas as pd

df1 = pd.read_csv('first_result.csv')
df2 = pd.read_csv('output_data.csv')



column_to_move = 'difficulty'
df2_subset = df2[['slug', column_to_move]]
merged_df=pd.merge(df2_subset, df1, left_on='slug', right_on='slug', how='left')

merged_df.to_csv('merged_file.csv', index=False)
print(merged_df.head())
"""

import math

import pandas as pd

df1 = pd.read_csv('merged_file.csv')

accept_ratio = (df1['status_msg'] == 'Accepted').mean()
print(f"'Accepted' proportion: {accept_ratio:.2%}")

perfect_ration = (df1['runtime_percentile'] == 100).mean()
print(f"'perfect_code' proportion: {perfect_ration:.2%}")

ratio = (
    df1.groupby('difficulty')['status_msg']
    .value_counts(normalize=True)
    .unstack(fill_value=0) * 100
)
print(ratio['Accepted'].round(2).astype(str) + '%')

ratio = (
    df1.groupby('difficulty')['runtime_percentile']
    .value_counts(normalize=True)
    .unstack(fill_value=0) * 100
)
print(ratio[100].round(2).astype(str) + '%')