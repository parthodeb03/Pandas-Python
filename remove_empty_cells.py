import pandas as pd
df = pd.read_csv('spotify_tracks.csv')
print(df.dropna().to_string())