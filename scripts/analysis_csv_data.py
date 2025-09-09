import pandas as pd

df = pd.read_csv("data/healthcare_dataset.csv")
df
print(df.info())
print(df.describe())

#Age
print(df["Age"].min())
print(df["Age"].max())

#Gender
print(df["Gender"].value_counts())

#Blood Type
print(df["Blood Type"].value_counts())
