import dataset
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def build_graph(edges_df, nodes_df):
    """
    Build a directed graph from the transport network.
    Nodes represent transport stops and include their attributes.
    Edges represent directed connections between consecutive stops.
    """

    G = nx.DiGraph()

    # Add nodes with attributes
    for _, row in nodes_df.iterrows():
        G.add_node(
            row["stop_I"],
            name=row["name"],
            lat=row["lat"],
            lon=row["lon"]
        )

    # Add directed edges
    for _, row in edges_df.iterrows():
        G.add_edge(
            row["from_stop_I"],
            row["to_stop_I"]
        )

    return G


def run_graph_overview():

    for city in dataset.CITIES:

        edges_df = dataset.load_network(city)
        nodes_df = dataset.load_nodes(city)

        G = build_graph(edges_df, nodes_df)

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

        edges_df = dataset.load_network(city)
        nodes_df = dataset.load_nodes(city)

        G = build_graph(edges_df, nodes_df)

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

        edges_df = dataset.load_network(city)
        nodes_df = dataset.load_nodes(city)

        G = build_graph(edges_df, nodes_df)

        distribution = get_degree_distribution(G)

        print(f"\n===== {city.upper()} =====")
        print("\nDegree distribution")
        print(distribution)

        plot_degree_distribution(distribution, city)


def get_average_clustering_coefficient(G):
    return nx.average_clustering(G)


def run_clustering_analysis():

    for city in dataset.CITIES:

        edges_df = dataset.load_network(city)
        nodes_df = dataset.load_nodes(city)

        G = build_graph(edges_df, nodes_df)

        clustering = get_average_clustering_coefficient(G)

        print(f"\n===== {city.upper()} =====")
        print(f"Average clustering coefficient: {clustering:.4f}")


def get_betweenness_centrality(G):
    return nx.betweenness_centrality(
        G,
        normalized=True
    )


def get_top_betweenness_nodes(centrality, nodes_df):
    """
    Return the top 10 nodes with the highest betweenness centrality.
    """

    top_nodes = (
        pd.DataFrame(
            centrality.items(),
            columns=["Stop ID", "Betweenness"]
        )
        .sort_values(
            by="Betweenness",
            ascending=False
        )
        .head(5)
    )

    top_nodes = top_nodes.merge(
        nodes_df[["stop_I", "name"]],
        left_on="Stop ID",
        right_on="stop_I",
        how="left"
    )

    top_nodes = (
        top_nodes
        .drop(columns="stop_I")
        .rename(columns={"name": "Stop Name"})
        .reset_index(drop=True)
    )

    top_nodes["Betweenness"] = (
        top_nodes["Betweenness"]
        .round(3)
    )

    return top_nodes


def run_betweenness_analysis():

    for city in dataset.CITIES:

        edges_df = dataset.load_network(city)
        nodes_df = dataset.load_nodes(city)

        G = build_graph(edges_df, nodes_df)

        centrality = get_betweenness_centrality(G)

        top_nodes = get_top_betweenness_nodes(
            centrality,
            nodes_df
        )

        print(f"\n===== {city.upper()} =====")
        print(top_nodes)


def run_average_degree_analysis():
    print("\n===== AVERAGE DEGREE =====\n")

    for city in dataset.CITIES:
        edges_df = dataset.load_network(city)
        nodes_df = dataset.load_nodes(city)

        G = build_graph(edges_df, nodes_df)

        avg_degree = (
            sum(dict(G.degree()).values())
            / G.number_of_nodes()
        )

        print(f"{city.upper()}: {avg_degree:.3f}")


def export_graph_gexf(G, city):
    """
    Export graph to GEXF format for Gephi.
    """

    output = Path("gephi") / f"{city}.gexf"

    output.parent.mkdir(exist_ok=True)

    nx.write_gexf(G, output)


def export_all_graphs():

    for city in dataset.CITIES:

        edges_df = dataset.load_network(city)
        nodes_df = dataset.load_nodes(city)

        G = build_graph(edges_df, nodes_df)

        export_graph_gexf(G, city)