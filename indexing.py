import pandas as pd

data = {
    "Bands":["Artcell", "Black", "Aurthohin"],
    "Tracks":["Bhul Jonmo", "Abar", "Chaite Paro"]
}

df = pd.DataFrame(data, index = ["R1","R2","R3"])
print(df)
