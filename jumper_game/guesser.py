import random
words = ("tree","mars","class", "scissor", "paper", "rock", "fire" )

class Guesser: 
    
    def __init__(self):
        self.random_word = ''
        self.word_with_placeholders = []

    def get_random_word(self):
        self.random_word = self.get_word()
        # copy the word and then wipe out ever letter with a _ 
        # so we have a place to stick guesses
        for i in range(len(self.random_word)):
            self.word_with_placeholders.append('_') 
        return 

    def get_word(self):
        word = random.choice(words)
        return word

    def check_guess(self, player_move):
        if player_move in self.random_word:
            for i, ch in enumerate(self.random_word):
                if ch == player_move:
                    self.word_with_placeholders[i]=player_move
            return True
        return False
    
    def get_word_with_placeholders(self):
       return "".join(self.word_with_placeholders)