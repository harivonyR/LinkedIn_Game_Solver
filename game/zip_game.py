# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 15:16:00 2025

@author: harivonyratefiarison
"""

import json
import os

# from core.browser import Browser
# from modules.linkedin_game.linkedin_nav import LinkedInNavigator
# from modules.linkedin_game.zip_solver import ZipGame

class ZipGame:
    def __init__(self, grid_data):
        self.grid = grid_data["grid"]["cells"]
        self.walls = grid_data["wall"]
        self.rows = grid_data["grid"]["rows"]
        self.cols = grid_data["grid"]["cols"]
        self.game_id = grid_data["gameId"]

    def solve(self):
        """
        Exemple : retourne une liste de tuples représentant le chemin trouvé.
        À remplacer par le véritable algorithme de résolution.
        """
        path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2)]
        return path

    def get_directions(self, path):
        """
        Convertit la solution en directions du clavier : haut, bas, gauche, droite
        """
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
        return directions


if __name__ == "__main__":
    
    # Charger la grille depuis le JSON d'entrée
    input_path = "data/input/zip_grid_142.json"
    with open(input_path, "r") as f:
        grid_data = json.load(f)

    # Initialiser le jeu
    zip_game = ZipGame(grid_data)

    # Résoudre la grille
    solution = zip_game.solve()
    directions = zip_game.get_directions(solution)

    # Préparer le résultat
    output_data = {
        "gameId": zip_game.game_id,
        "solution": solution,
        "direction": directions
    }

    # Exporter la solution
    os.makedirs("data/solution", exist_ok=True)
    output_path = f"data/solution/{zip_game.game_id}.json"
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)

    print(f"✅ Solution enregistrée dans {output_path}")
