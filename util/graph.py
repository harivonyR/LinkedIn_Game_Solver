# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 20:52:55 2025

@author: Lenovo
"""

# util/graph.py
def get_graph(grid, walls):
    rows, cols = len(grid), len(grid[0])
    graph = {}

    # Transformer les murs en set de paires de tuples pour vérification rapide
    wall_set = set(tuple(map(tuple, w)) for w in walls)

    def is_wall(a, b):
        return (a, b) in wall_set or (b, a) in wall_set

    for r in range(rows):
        for c in range(cols):
            neighbors = []
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if not is_wall((r, c), (nr, nc)):
                        neighbors.append((nr, nc))
            graph[(r, c)] = neighbors

    return graph
