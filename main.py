from load_dataset import load_steam_dataset
from heatmap_data import create_heatmap_dataset, split_tags, count_games, create_heatmap_matrix, filter_top_tags
from heatmap_visalisation import create_genre_heatmap

def main():
    file_path = "Dataset/games_march2025_cleaned.csv"

    df = load_steam_dataset(file_path)

    heatmap_df = create_heatmap_dataset(df)
    heatmap_df = split_tags(heatmap_df)

    tag_counts = count_games(heatmap_df)
    heatmap_matrix = create_heatmap_matrix(tag_counts)
    filter_heatmap_matrix = filter_top_tags(heatmap_matrix, 30)

    fig = create_genre_heatmap(filter_heatmap_matrix)
    fig.show()

if __name__ == '__main__':
    main()