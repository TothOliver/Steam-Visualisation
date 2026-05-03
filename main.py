from load_dataset import load_steam_dataset
from heatmap_data import create_heatmap_dataset, split_tags, prepare_heatmap_data
from scatter_data import create_scatter_dataset, filter_top_tags_scatter
from heatmap_visalisation import create_tag_heatmap 
from scatter_visualisation import create_scatter

def main():

    #Load
    file_path = "Dataset/games_march2025_cleaned.csv"
    df = load_steam_dataset(file_path)

    #Heatmap
    heatmap_data = prepare_heatmap_data(df, top_n=30)

    fig1 = create_tag_heatmap(
        heatmap_data["default_heatmap_matrix"], 
        heatmap_data["default_percentage_matrix"])
    fig1.show()

    #Scatter
    scatter_df = create_scatter_dataset(df)
    scatter_df = split_tags(scatter_df)

    filtered_df = filter_top_tags_scatter(scatter_df, 30)

    fig2 = create_scatter(filtered_df)
    fig2.show()



if __name__ == '__main__':
    main()

