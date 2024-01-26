import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappop, heappush


def dijkstra(G, start):
    if start not in G:
        raise ValueError(f"Graph doesn't contain node {start}")

    pq = []  # Binary heap
    visited = set()  # List of already visited nodes
    # Dictionary of shortest distance from start to each node
    dist_to = {v: float('inf') for v in G.nodes}

    # Add start node to heap
    dist_to[start] = 0
    heappush(pq, (0, start))

    # While there are nodes to visit
    while pq:
        # Get the node with the smallest distance
        dist, u = heappop(pq)

        # If the node is already visited, skip it
        if u in visited:
            continue

        # Add the node to the visited list
        visited.add(u)

        # Update the distances of the neighbors
        for source, target, weight in G.edges(u, data='weight'):
            if source == u:
                new_dist = dist + weight
                if new_dist < dist_to[target]:
                    dist_to[target] = new_dist
                    heappush(pq, (new_dist, target))

    return dist_to


if __name__ == "__main__":
    G = nx.Graph()
    G.add_nodes_from(['A', 'B', 'C', 'D'])
    G.add_weighted_edges_from([
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 3),
    ])

    start = 'A'

    dist_to = dijkstra(G, start)

    # Print the shortest distance to each node
    for v in G.nodes:
        if v == start:
            continue
        print(f"Shortest path from {start} to {v}: {dist_to[v]}")

    # Visualize the graph
    pos = nx.spring_layout(G)  # Positioning of nodes
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges})
    plt.show()
