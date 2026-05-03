from load_dataset import load_steam_dataset
from heatmap_data import create_heatmap_dataset, split_tags, count_games, create_heatmap_matrix, filter_top_tags, create_scatter_dataset, filter_top_tags_scatter
from heatmap_visalisation import create_genre_heatmap, create_scatter

def main():

    #Load
    file_path = "Dataset/games_march2025_cleaned.csv"
    
    df = load_steam_dataset(file_path)

    #Heatmap

    heatmap_df = create_heatmap_dataset(df)
    heatmap_df = split_tags(heatmap_df)
    tag_counts = count_games(heatmap_df)
    heatmap_matrix = create_heatmap_matrix(tag_counts)
    
    filter_heatmap_matrix = filter_top_tags(heatmap_matrix, 30)

    fig = create_genre_heatmap(filter_heatmap_matrix)
    fig.show()

    #Scatter

    scatter_df = create_scatter_dataset(df)
    scatter_df = split_tags(scatter_df)

    filtered_df = filter_top_tags_scatter(scatter_df, 30)

    fig = create_scatter(filtered_df)
    fig.show()

if __name__ == '__main__':
    main()

