import dataset
import networkx as nx


def build_graph(df):
    """
    Build a directed graph from the transport network.
    Nodes represent stops.
    Edges represent connections between stops.
    """

    return nx.from_pandas_edgelist(
        df,
        source="from_stop_I",
        target="to_stop_I",
        create_using=nx.DiGraph()
    )


def run_graph_overview():

    for city in dataset.CITIES:

        df = dataset.load_network(city)

        G = build_graph(df)

        print(f"\n===== {city.upper()} =====")
        print("nodes:", G.number_of_nodes())
        print("edges:", G.number_of_edges())