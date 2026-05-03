from load_dataset import load_steam_dataset
from heatmap_data import create_heatmap_dataset, split_tags, count_games, create_heatmap_matrix, filter_top_tags, create_percentage_matrix
from scatter_data import create_scatter_dataset, filter_top_tags_scatter
from heatmap_visalisation import create_tag_heatmap 
from scatter_visualisation import create_scatter

def main():

    #Load
    file_path = "Dataset/games_march2025_cleaned.csv"
    df = load_steam_dataset(file_path)

    #Heatmap
    heatmap_matrix, percentage_matrix = prepare_heatmap_data(df, top_n=30)

    fig1 = create_tag_heatmap(heatmap_matrix, percentage_matrix)
    fig1.show()

    #Scatter
    scatter_df = create_scatter_dataset(df)
    scatter_df = split_tags(scatter_df)

    filtered_df = filter_top_tags_scatter(scatter_df, 30)

    fig2 = create_scatter(filtered_df)
    fig2.show()

def prepare_heatmap_data(df, top_n=30):
    heatmap_df = create_heatmap_dataset(df)
    heatmap_df = split_tags(heatmap_df)

    tag_counts = count_games(heatmap_df)
    heatmap_matrix = create_heatmap_matrix(tag_counts)

    percentage_matrix = create_percentage_matrix(heatmap_matrix, heatmap_df)
    filtered_heatmap_matrix = filter_top_tags(heatmap_matrix, top_n)
    filtered_percentage_matrix = percentage_matrix[filtered_heatmap_matrix.columns]


    return filtered_heatmap_matrix, filtered_percentage_matrix

if __name__ == '__main__':
    main()

