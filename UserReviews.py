import pandas as pd

df = pd.read_csv("user_reviews.csv")
df['len_txt'] = df['text'].apply(len)  # add a len_txt column to the dataframe and content
print(df.head())  # display all heads in the df for checking above adding new column is success or not


def super_Category(value):
    while True:
        if value['len_txt'] > 1000 or value['grade'] >= 9:  # function for checking those conditions and create the
            # column
            return 'expert reviewer'
        elif value['grade'] <= 1 and value['len_txt'] > 1000:
            return 'opposed reviewer'
        else:
            return 'neutral reviewer'


df['super category'] = df.apply(super_Category, axis=1)  # add column to the df, and content
print(df.head())  # display all columns in df
