import pandas as pd

df = pd.read_csv("data.csv")


df = df[df["target"] == 1]


df = df.drop(columns=["target"])

df.to_csv("data_filtered.csv", index=False)
