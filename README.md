# Final project for intro to DS subject.

This is the repo for python implementation of data cleaning and splitting a dataset.

The data that is used is `data.csv` file.

## Data cleaning

Here we drop column if it passes one of the conditions
- There is only one unique number in column.
- Number of missing values is higher than 80% of data size.
- Column contains strings and number of unique values is more than 60.


## Column type detection

Here we identidy categorical and numerical columns as follows
- If a column contains only numbers and its number of unique values is more than 60, it is identified as numeric.
- Otherwise, it is identified as categorical.


## Missing values

Here we go over the numeric columns, and fill missing values with the mean of the column.


## Categorical preprocessing

As we have a lot of categorical values, and some of them has high cardinality, we keep only the top 70% of categorical values, and assign `Other` to the rest.

## Dummy encoding

We go over the categorical columns and apply dummy encoding to all of them.

## Splitting
We split the data by 0.8(train)/0.2(test) and save them in train.csv, test.csv files