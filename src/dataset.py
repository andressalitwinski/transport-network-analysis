import pandas as pd

CITIES = [
    "lisbon",
    "paris",
    "luxembourg"
]

def load_network(city):
    return pd.read_csv(
        f"data/{city}/network_combined.csv",
        sep=";"
    )


def count_edges(df):
    return len(df)


def count_nodes(df):
    return len(
        set(df["from_stop_I"]).union(
            set(df["to_stop_I"])
        )
    )


def get_route_types(df):
    """
    Find out what types of transportation are available in each city
    """
    return df["route_type"].value_counts().sort_index()


def get_bidirectional_edge_stats(df):
    """
    Count edges that have an explicit reverse edge and compute the percentage of bidirectional links
    """

    edges = set(
        zip(
            df["from_stop_I"],
            df["to_stop_I"]
        )
    )

    reverse_count = 0

    for u, v in edges:
        if (v, u) in edges:
            reverse_count += 1

    percentage = 100 * reverse_count / len(edges)

    return reverse_count, percentage