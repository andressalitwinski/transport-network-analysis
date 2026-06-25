import dataset
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


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


def get_degree_distribution(G):
    """
    Compute the degree distribution of the graph.
    Returns a DataFrame with:
        - Degree
        - Count
    """

    degrees = [degree for _, degree in G.degree()]

    distribution = (
        pd.Series(degrees)
        .value_counts()
        .sort_index()
        .reset_index()
    )

    distribution.columns = ["Degree", "Count"]

    return distribution


def plot_degree_distribution(distribution, city):

    plt.figure(figsize=(8, 5))

    plt.bar(
        distribution["Degree"],
        distribution["Count"]
    )

    plt.title(f"Degree Distribution - {city.capitalize()}")
    plt.xlabel("Degree")
    plt.ylabel("Number of Nodes")

    # Show only existing degree values on the x-axis
    plt.xticks(distribution["Degree"])

    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.show()


def run_degree_analysis():

    for city in dataset.CITIES:

        df = dataset.load_network(city)

        G = build_graph(df)

        distribution = get_degree_distribution(G)

        print(f"\n===== {city.upper()} =====")
        print("\nDegree distribution")
        print(distribution)

        plot_degree_distribution(distribution, city)