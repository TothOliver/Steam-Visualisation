from load_dataset import load_steam_dataset, create_heatmap_dataset

file_path = "Dataset/games_march2025_cleaned.csv"

df = load_steam_dataset(file_path)

heatmap_df = create_heatmap_dataset(df)

print("\nFULL DATASET")
print(df.shape)

print("\nHEATMAP DATASET")
print(heatmap_df.shape)

print("\nFIRST 5 ROWS")
print(heatmap_df.head())

print("\nMISSING VALUES")
print(heatmap_df.isna().sum())