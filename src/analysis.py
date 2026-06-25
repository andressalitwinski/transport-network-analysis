import dataset
import networkx as nx


def build_graph(df):
    """
    Build a directed graph from the transport network.
    Nodes represent stops.
    Edges represent connections between stops.
    """

    # each row of the dataset is converted into a directed edge
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


def get_scc_statistics(G):
    """
    Compute statistics about strongly connected components.
    Returns:
        - number of SCCs
        - size of the largest SCC
        - percentage of nodes in the largest SCC    
    """

    sccs = list(nx.strongly_connected_components(G))

    num_components = len(sccs)
    largest_component_size = max(len(component) for component in sccs)
    largest_component_percentage = (
        100 * largest_component_size / G.number_of_nodes()
    )

    return num_components, largest_component_size, largest_component_percentage


def run_connectivity_analysis():

    for city in dataset.CITIES:

        df = dataset.load_network(city)

        G = build_graph(df)

        num_components, largest_component_size, largest_component_percentage = get_scc_statistics(G)

        print(f"\n===== {city.upper()} =====")
        print("\nStrongly Connected Components")
        print("count:", num_components)
        print("largest:", largest_component_size)
        print("largest (%):", f"{largest_component_percentage:.2f}%")