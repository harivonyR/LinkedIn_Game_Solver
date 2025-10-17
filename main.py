# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 11:00:43 2025

@author: harivonyratefiarison
"""

#from core.browser import Browser
#from modules.linkedin_game.linkedin_nav import LinkedInNavigator
from modules.linkedin_game.zip_solver import ZipGame


if __name__ == "__main__":
    #browser = Browser(headless=False)
    #browser.start()

    try:
        #linkedin = LinkedInNavigator(browser)
        #linkedin.login("email", "password")
        #linkedin.open_zip_game()

        #zip_game = ZipGame(browser)
        grid = 
        zip_game = ZipGame
        solution = zip_game.solve()
        commands = zip_game.get_command(solution)
        zip_game.press_command(commands)

    finally:
        browser.quit()
