#!/usr/bin/env python3

"""
This program will read in the project/people data in data.csv and 
project it into two separate graphs and save the edge lists with
their weights in projects.csv and people.csv.
"""

import csv
import igraph

data = csv.reader(open("data.csv"))
g = igraph.Graph()

for row in data:
    g.add_vertex(row[0], is_project=True)
    g.add_vertex(row[1], is_project=False)
    g.add_edge(row[0], row[1])

g1, g2 = g.bipartite_projection(types="is_project")

def output(graph, filename):
    out = csv.writer(open(filename, "w"))
    for edge in graph.es():
        out.writerow([
            graph.vs(edge.source)['name'][0],
            graph.vs(edge.target)['name'][0], 
            edge['weight']
        ])

output(g1, "people.csv")
output(g2, "projects.csv")
