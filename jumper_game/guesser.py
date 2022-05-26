import random

class Guesser: 
    words = ("tree","mars","class", "scissor", "papper", "rock", "fire" )
    def __init__(self):
        self.random = ''

    def get_ramdom_word(self):
        self.random = self.get_word()

    def get_word(self):
        word = random.choice(self.words)
        return word

    def guess(self,letter):
        indices_of_letter = []
        for i, ch in enumerate(self.random):
            if ch == letter:
                indices_of_letter.append(i)
        temp = indices_of_letter
        return temp


