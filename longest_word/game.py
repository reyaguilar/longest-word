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


        letters = self.grid.copy()
        for letter in word.upper():
            if letter in letters:
                letters.remove(letter)
            else:
                return False


        try:
            response = requests.get(
                f"https://dictionary.lewagon.com/{word.lower()}"
            )
        except requests.RequestException:
            return False

        if response.status_code != 200:
            return False

        data = response.json()


        is_valid_flag = data.get("found")
        if is_valid_flag is None:
            is_valid_flag = data.get("valid")

        return bool(is_valid_flag)
