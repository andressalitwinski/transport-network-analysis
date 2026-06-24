# Transport Network Analysis

Comparative network science analysis of public transport systems in Lisbon, Paris and Luxembourg.

## Overview

This project investigates the structural properties of public transport networks using concepts from Network Science.

The study compares three European cities with different network scales and characteristics:

* Lisbon (Portugal)
* Paris (France)
* Luxembourg (Luxembourg)

The objective is to analyze and compare their network topology, connectivity, centrality patterns, and community structure.

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
├── src/
│   ├── main.py
│   ├── dataset.py
│   ├── eda.py
│   └── analysis.py
│
├── report/
│
├── README.md
└── .gitignore
```

## Current Status

* [x] Dataset selection
* [x] Dataset exploration
* [ ] Network construction
* [ ] Connectivity analysis
* [ ] Centrality analysis
* [ ] Community detection
* [ ] Visualization with Gephi
* [ ] Final report

## Technologies

* Python
* Pandas
* NetworkX
* Gephi
* LaTeX (Overleaf)

## Academic Context

This project was developed as the final project for a Network Science course at the Faculty of Sciences, University of Porto (FCUP).

## Author

Andressa Litwinski
