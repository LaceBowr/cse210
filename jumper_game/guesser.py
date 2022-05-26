import random

class Guesser: 
    words = ("tree","mars","class", "scissor", "papper", "rock", "fire" )
    def __init__(self):
        self.random = ''

    def get_random_word(self):
        self.random = self.get_word()
        return word

    def get_word(self):
        word = random.choice(self.words)
        return word

    def check_guess(self, player_move):
        indices_of_letter = []
        for i, ch in enumerate(self.random):
            if ch == player_move:
                indices_of_letter.append(i)
        temp = indices_of_letter
        return True
    
    def get_word_with_placeholders(self):
        return self._word_with_placeholders


