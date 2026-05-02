from load_dataset import load_steam_dataset
from heatmap_data import create_heatmap_dataset, split_genres

file_path = "Dataset/games_march2025_cleaned.csv"

df = load_steam_dataset(file_path)

heatmap_df = create_heatmap_dataset(df)
heatmap_df = split_genres(heatmap_df)

print("\nUNIQUE GENRES")
unique_genres = sorted(heatmap_df["genre"].unique())
print("Number of unique genres:", len(unique_genres))
print(unique_genres)
