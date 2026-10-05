import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport

df = pd.read_csv("studentperformance.csv")

print(df[["student name"]])

top3 = df["final score"].nlargest(3)
print(top3)

print(df[["student name", "final score"]].head(3))

print(df["final score"].sort_values())

print(df["final score"].sort_values(ascending=False))

print(df.sort_values("final score", ascending=False))

print(df.describe())

print(df.corr(numeric_only=True))

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()


print(df["final score"] > 50)

print(df[df["final score"] > 50])

print(df[df["gender"] == "Female"])


print(df[
    (df["gender"] == "Female") |
    (df["gender"] == "Male")
])

print(df["gender"].isin(["Female", "Male"]))

print(df[df["gender"].isin(["Female", "Male"])])


profile = ProfileReport(
    df,
    title="My Data Report",
    explorative=True
)

print(profile)