import pandas as pd

df = pd.read_csv('spotify_tracks.csv')

new_row = pd.DataFrame([{
    "id": "7kr3xZk1ys3YSZ4VFta2Bt",
    "name": "Megadeth",
    "genre": "HEAVY-METAL",
    "artists": "Megadeth",
    "album": "Killing Is My Business",
    "popularity": 60,
    "duration_ms": 4908,
    "explicit": True
}])

if new_row["id"].iloc[0] not in df["id"].values:
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv('spotify_tracks.csv', index=False)
    print("Row inserted and saved to CSV.")
else:
    print("Track already exists in CSV — nothing inserted.")

print(df.tail())
