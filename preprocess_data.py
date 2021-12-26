import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('data.csv')

drop_cols = []
nan_thresh = 0.8
cat_limit = 60
cat_cols = []
num_cols = []

for col in df:
    if len(df[col].unique()) == 1:
        drop_cols.appdne(col)
    elif df[col].isna().sum() > df.shape[0]*nan_thresh:
        drop_cols.append(col)
    elif df[col].dtype == object and len(df[col].unique()) >= cat_limit:
        drop_cols.append(col)
    
clean_df = df.drop(drop_cols, axis=1)
for col in clean_df:
    if df[col].dtype != object and len(df[col].unique()) >= cat_limit:
        num_cols.append(col)
    else:
        cat_cols.append(col)

for col in num_cols:
    clean_df[col] = clean_df[col].fillna(clean_df[col].mean())

dummy_thresh = 10
top_cat_ratio = 0.7
for col in cat_cols:
    value_counts = clean_df[col].value_counts()
    if value_counts.shape[0] > dummy_thresh:
        to_mask = value_counts.iloc[int(value_counts.shape[0]*top_cat_ratio):].index.tolist()
        ids = clean_df[col][clean_df[col].isin(to_mask)].index
        clean_df[col].iloc[ids] = 'Other'

clean_df = pd.get_dummies(clean_df, columns=cat_cols)

train_df, test_df = train_test_split(clean_df, test_size=0.2)
train_df.to_csv('train.csv', index=False)
test_df.to_csv('test.csv', index=False)

