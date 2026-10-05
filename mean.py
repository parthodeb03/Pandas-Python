import pandas as pd
df = pd.read_csv('spotify_tracks.csv')
x = df["name"].mode()
print(x)