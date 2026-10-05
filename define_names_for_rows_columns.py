import pandas as pd

students = ["Alice","Bob","Charlie"]

df = pd.DataFrame(students,columns=["Students"],index=["r1","r2","r3"])

print(df)