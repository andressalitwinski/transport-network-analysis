import dataset


def count_duplicate_edges(df):
    """
    Count duplicated edges in the raw dataset.
    """
    total_edges = len(df)

    unique_edges = len(
        df[["from_stop_I", "to_stop_I"]]
        .drop_duplicates()
    )

    duplicates = total_edges - unique_edges

    return duplicates


def run_duplicate_edge_analysis(df):
    # Show repeated edges and their transport types
    duplicates = df[
        df.duplicated(
            subset=["from_stop_I", "to_stop_I"],
            keep=False
        )
    ]

    print(
        duplicates[
            ["from_stop_I", "to_stop_I", "route_type"]
        ]
        .sort_values(["from_stop_I", "to_stop_I"])
        .head(20)
    )


def run_dataset_overview():

    for city in dataset.CITIES:

        df = dataset.load_network(city)

        print(f"\n===== {city.upper()} =====")

        # print(df.head())
        # print(df.columns)
        # print(df.shape)
        # print(df.isnull().sum())

        # nodes = pd.read_csv("lisbon/network_nodes.csv")
        # print(nodes.head())
        # print(nodes.columns)
        # print(nodes.shape)
 
        # ver se as cidades tem as mesmas colunas
        # print(list(df.columns))

        print("nodes:", dataset.count_nodes(df))
        print("edges:", dataset.count_edges(df))

        print("\nRoute types:")
        print(dataset.get_route_types(df))

        reverse_count, percentage = dataset.get_bidirectional_edge_stats(df)

        print("\nBidirectional edges:")
        print("reverse:", reverse_count)
        print("percentage:", f"{percentage:.2f}%")

        print("duplicated edges:", count_duplicate_edges(df))
        run_duplicate_edge_analysis(df)