# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 11:00:43 2025

@author: harivonyratefiarison
"""

from game.zip_game import ZipGame
import json

if __name__ == "__main__":
    input_path = "data/input/zip_grid_142.json"

    with open(input_path, "r") as f:
        grid_data = json.load(f)

    zip_game = ZipGame(grid_data)
    zip_game.solve()
    zip_game.export_solution()
