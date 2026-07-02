# Transport Network Analysis

Comparative network science analysis of public transport systems in Lisbon, Paris and Luxembourg.

## Overview

This project presents a comparative Network Science analysis of public transport networks in Lisbon, Paris and Luxembourg.

The networks were modelled as directed graphs and analysed through complementary structural measures, including connectivity, degree distribution, clustering coefficient, betweenness centrality and community detection.

The goal was to investigate how transport networks of different scales differ in terms of connectivity, centralization and community structure.

## Dataset

This project uses the dataset introduced in:

Kujala, R., Weckström, C., Darst, R. K., Mladenović, M. N., & Saramäki, J. (2018).

**A Collection of Public Transport Network Data Sets for 25 Cities.**

Scientific Data, 5, 180089.

DOI: https://doi.org/10.1038/sdata.2018.89

The dataset contains multimodal public transport networks extracted from GTFS feeds and includes information about stops, routes, travel times, distances, and transportation modes.

Due to its size, the raw dataset is not included in this repository.

## Project Structure

```text
transport-network-analysis/
│
├── data/
│
├── gephi/
│
├── report/
│   └── img/
│
├── src/
│   ├── main.py
│   ├── dataset.py
│   ├── eda.py
│   └── analysis.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Current Status

- [x] Dataset selection
- [x] Dataset exploration (EDA)
- [x] Directed graph construction
- [x] Connectivity analysis (Strongly Connected Components)
- [x] Degree distribution analysis
- [x] Clustering coefficient analysis
- [x] Betweenness centrality analysis
- [x] Export graphs for Gephi
- [x] Community detection (Gephi)
- [x] Network visualization (Gephi)
- [x] Final report

## Main Findings

The analysis revealed substantial structural differences between the three transport networks.

- Luxembourg exhibits the highest level of connectivity, with 99.5% of nodes belonging to the largest strongly connected component.
- Lisbon presents the highest level of fragmentation, with only 36.3% of nodes belonging to the largest strongly connected component.
- Paris occupies an intermediate position between the two networks.
- Luxembourg shows a substantially higher average degree (4.72) and clustering coefficient (0.0726) than Lisbon and Paris.
- Betweenness centrality highlights a strong dependence on a small number of strategic transport hubs in Luxembourg, particularly Luxembourg Gare Centrale.
- Community detection revealed strong modular structures in all three cities, with modularity values above 0.86.

## Technologies

* Python
* Pandas
* NetworkX
* Matplotlib
* Gephi
* LaTeX (Overleaf)

## Academic Context

This project was developed as the final project for a Network Science course at the Faculty of Sciences, University of Porto (FCUP).

## Author

Andressa Litwinski
