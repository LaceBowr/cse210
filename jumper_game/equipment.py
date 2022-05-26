#from guesser import Guesser
# Equipment should not need to know about words or anything.
parachute = "   _____ \n,  /_____\ \n  \     / \n   \   / "
skydiver = "     0 \n    /|\ \n    / \ "
class Equipment(object):
 
    #The execution of actions or no-actions for the jumper
    def __init__(self):
        #get_word = Guesser()
        self.parachute = '   _____  \n  /_____\ \n  \     / \n   \   / '
        self.skydiver = "    0 \n    /|\ \n    / \ "
        #self._word = ""
        #self._word = get_word.get_word_with_placeholders()
        #self.letters = get_word.get_random_word()
 
    def blast_parachute(self):
        if len(self.parachute) > 11:
            self.parachute=self.parachute[11:]
        else:
            self.parachute = ''
        if not self.parachute:
            self.skydiver = self.skydiver.replace("    0 \n","    X \n")
        return self.parachute+self.skydiver
 
    def parachute_is_safe(self):
        if len(self.parachute) > 0:
            return True
        return False
 
    """def print_word_with_spaces(word):
        guessed_words = []    
        word_completion = '_' * len(word)
        tries = 4
        print(word_completion)
        while tries > 5:
            if word_with_placeholder == player_move and """
 
    def get_jumper(self):
        display_jumper = f'{self.parachute} \n {self.skydiver} \n'
        return display_jumper
