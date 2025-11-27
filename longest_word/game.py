import string
import random
import requests

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))


    def is_valid(self, word):
        if not word:
            return False

        #Check the word can be built from the grid
        letters = self.grid.copy()  # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False

        #Check the word is in the English dictionary
        response = requests.get(
            f"https://wagon-dictionary.herokuapp.com/{word.lower()}"
        )
        if response.status_code != 200:
            return False

        data = response.json()
        return data.get("found", False)
