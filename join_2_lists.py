import pandas as pd

list_1 = ["Alice","Bob","Charlie"]
list_2 = [3.75,3.88,4.00]

df = pd.DataFrame(zip(list_1,list_2),columns=["Students","CGPA"])
print(df)