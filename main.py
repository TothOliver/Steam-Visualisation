from load_dataset import load_steam_dataset
from heatmap_data import create_heatmap_dataset, split_tags, count_games, create_heatmap_matrix
from heatmap_visalisation import create_genre_heatmap

file_path = "Dataset/games_march2025_cleaned.csv"

df = load_steam_dataset(file_path)

heatmap_df = create_heatmap_dataset(df)
heatmap_df = split_tags(heatmap_df)
