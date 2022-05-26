from guesser import Guesser
from jumper_game.jumperdirector import Director
 
class Equipment(object):
    def __init__(self):
        self.parachute="   _____ \n"+"  /_____\ \n"+"  \     / \n"+"   \   / "
        self.skydiver="     0 \n"+"    /|\ \n"+"    / \ "
        get_word=Guesser()
        player_move=Director()
        self.move=player_move._input_administrator()
        self._word=""
        self._word=get_word.get_word_with_placeholders()
        self.letters=get_word.guess()
 
    def blast_parachute(self):
        # removes a line from the jumper
        n=0
        while n != 5:
            if self._word not in self.letters:
                parachute=self.parachute[10:]
                return parachute
            if n >= 4:
                skydiver=skydiver.replace("     0 \n","     X \n")
                print(skydiver)
                print("gameover")
            return skydiver
 
    def parachute_is_safe(self,word):
 
        for letter in word:
            if letter.lower() == True:
                print(letter,end= " ")
            else:
                print("_",end=" ")
   
