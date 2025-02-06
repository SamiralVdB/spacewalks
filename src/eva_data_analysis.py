import matplotlib.pyplot as pltimport pandas as pdimport sysimport osdef main(input_file: str,         output_file: str,         graph_file: str) -> None:    print("--START--")    eva_df = read_json_file_to_dataframe(input_file)    write_dataframe_to_csv(eva_df, output_file)    plot_cumulative_time_in_space(eva_df, graph_file)    print("--END--")def read_json_file_to_dataframe(input_file:str) -> pd.DataFrame:    """    Read the data from a JSON file into a Pandas dataframe.    Clean the data by removing any incomplete rows and sort by date    Args:        input_file (str): The path to the JSON file.    Returns:        eva_df (pd.DataFrame): The cleaned and sorted data as a dataframe structure    """    print('Reading the following json file: ', input_file)    eva_df = pd.read_json(input_file, convert_dates=['date'])    eva_df['eva'] = eva_df['eva'].astype(float)    eva_df.dropna(axis=0, inplace=True)    eva_df.sort_values('date', inplace=True)    return eva_dfdef write_dataframe_to_csv(eva_df: pd.DataFrame, output_file: str) -> None:    """    Saving a dataframe to a csv file.    Args:        eva_df (pd.DataFrane): the dataframe to save        output_file (str): the location where the dataframe is saved    Returns:        None    """    print('Saving to ', output_file)    eva_df.to_csv(output_file, index=False)def text_to_duration(duration: str):    """    Convert a text format duration "HH:MM" to duration in hours    Args:        duration (str): The text format duration    Returns:        duration_hours (float): The duration in hours    """    hours, minutes = duration.split(":")    duration_hours = int(hours) + int(minutes)/60  # 60 minutes in an hour    return duration_hoursdef add_duration_hours_variable(df: pd.DataFrame):    """    Add duration in hours (duration_hours) variable to the dataset    Args:        df (pd.DataFrame): The input dataframe.    Returns:        df_copy (pd.DataFrame): A copy of df_ with the new duration_hours variable added    """    df_copy = df.copy()    df_copy["duration_hours"] = df_copy["duration"].apply(        text_to_duration    )    return df_copydef calculate_cumulative_hours_in_space(df: pd.DataFrame) -> pd.DataFrame:    """    Calculate the total hours spend in space at  specific data based on the duration in hh:mm format.    Args:        df (pd.DataFrame): the dataframe containing information about the time spend in space. Needs to have a column called 'duration'    Returns:        eva_df (pd.DataFrame): the dataframe with information about the cumulative hours spend in space    Raises:        KeyError: if input df does not contain the column 'duration'    """    df = add_duration_hours_variable(df)    df['cumulative_time'] = df['duration_hours'].cumsum()    return dfdef plot_cumulative_time_in_space(df: pd.DataFrame,                                  graph_file:str) -> None:    """    Calculate and plot the total time spend in space on a single day and save it to a graph file    Args:        df (pd.DataFrame): the dataframe containing information about the time spend in space. Needs to have a column called 'duration'        graph_file (str): the path to the output file in which the plot is saved    Returns:         None    Raises:        KeyError: if input df does not contain the column 'duration'    """    df = calculate_cumulative_hours_in_space(df)    print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')    plt.plot(df['date'], df['cumulative_time'], 'ko-')    plt.xlabel('Year')    plt.ylabel('Total time spent in space to date (hours)')    plt.tight_layout()    plt.savefig(graph_file)    plt.show()if __name__ == "__main__":    if len(sys.argv) < 3:        input_file = os.path.join('data', 'raw', 'eva-data.json')        output_file = os.path.join('data', 'processed', 'eva-data.csv')        print(f'Using default input and output filenames')    else:        input_file = sys.argv[1]        output_file = sys.argv[2]        print('Using custom input and output filenames')    graph_file = os.path.join('results','cumulative_eva_graph.png')    main(input_file, output_file, graph_file)