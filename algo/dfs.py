# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 20:52:21 2025

@author: Lenovo
"""

import json
from util.graph import get_graph

# algo/dfs.py
# algo/dfs.py
# -*- coding: utf-8 -*-
"""
DFS solver for Zip Game - full grid traversal with number ordering & wall constraints
"""
def dfs_solve_full(grid, graph):
    rows, cols = len(grid), len(grid[0])

    # Find all numbered cells
    numbered = sorted(
        [(r, c, grid[r][c]) for r in range(rows) for c in range(cols) if grid[r][c] > 0],
        key=lambda x: x[2]
    )
    last_value = numbered[-1][2]
    start = (numbered[0][0], numbered[0][1])

    total_cells = rows * cols
    visited = set()
    path = []

    def dfs(node, current_value):
        path.append(node)
        visited.add(node)

        # If we reached the final number and covered all cells → success
        if grid[node[0]][node[1]] == last_value and len(visited) == total_cells:
            return True

        # If on a numbered cell, advance order constraint
        if grid[node[0]][node[1]] == current_value + 1:
            current_value += 1

        for nb in graph[node]:
            if nb in visited:
                continue
            nb_val = grid[nb[0]][nb[1]]
            # Skip cells that jump too far ahead in numbering
            if nb_val > 0 and nb_val > current_value + 1:
                continue

            if dfs(nb, current_value):
                return True

        visited.remove(node)
        path.pop()
        return False

    dfs(start, 1)
    return path




if __name__ == "__main__":

    input_path = "data/input/zip_grid_142.json"

    with open(input_path, "r") as f:
        grid_data = json.load(f)
        
    grid = grid_data["grid"]["cells"]
    wall = grid_data["wall"]
    graph = get_graph(grid, wall)

    # find the order of the number
    rows, cols = len(grid), len(grid[0])
    
    numbered_cells = sorted(
        [(r, c, grid[r][c]) for r in range(rows) for c in range(cols) if grid[r][c] > 0],
        key=lambda x: x[2]
    )
    
    path = []
    visited = set()

    def dfs(current, target_val):
        """Parcours entre la cellule actuelle et la suivante dans l'ordre"""
        if grid[current[0]][current[1]] == target_val:
            path.append(current)
            return True

        visited.add(current)
        path.append(current)

        for neighbor in graph[current]:
            r, c = neighbor
            if neighbor not in visited and grid[r][c] >= 0:  # éviter les murs logiques
                if dfs(neighbor, target_val):
                    return True

        path.pop()
        visited.remove(current)
        return False