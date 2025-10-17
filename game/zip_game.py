# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 15:16:00 2025
@author: harivonyratefiarison
"""

import json
import os
from util.graph import get_graph
from algo.dfs import dfs_solve_full


class ZipGame:
    def __init__(self, grid_data):
        self.grid = grid_data["grid"]["cells"]
        self.walls = grid_data["wall"]
        self.rows = grid_data["grid"]["rows"]
        self.cols = grid_data["grid"]["cols"]
        self.game_id = grid_data["gameId"]
        self.graph = get_graph(self.grid, self.walls)
        self.solution = []
        self.directions = []

    def get_solution(self):
        self.solution = dfs_solve_full(self.grid, self.graph)
        return self.solution

    def get_directions(self, path):
        directions = []
        for i in range(1, len(path)):
            r1, c1 = path[i - 1]
            r2, c2 = path[i]
            if r2 == r1 + 1:
                directions.append("down")
            elif r2 == r1 - 1:
                directions.append("up")
            elif c2 == c1 + 1:
                directions.append("right")
            elif c2 == c1 - 1:
                directions.append("left")
        self.directions = directions
        return directions

    def solve(self):
        self.get_solution()
        self.get_directions(self.solution)
        return self.solution, self.directions
    
    def export_solution(self):
        output_data = {
            "gameId": self.game_id,
            "grid": self.grid,
            "walls": self.walls,
            "solution": self.solution,
            "directions": self.directions
        }

        os.makedirs("data/solution", exist_ok=True)
        output_path = f"data/solution/{self.game_id}.json"
        
        with open(output_path, "w") as f:
            json.dump(output_data, f, indent=2)
            
        print(f"✅ Solution enregistrée dans {output_path}")

if __name__ == "__main__":
    input_path = "data/input/zip_grid_143.json"

    with open(input_path, "r") as f:
        grid_data = json.load(f)

    zip_game = ZipGame(grid_data)
    zip_game.solve()
    zip_game.export_solution()

    

    

    
