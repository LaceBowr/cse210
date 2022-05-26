from guesser import Guesser


class Equipment(object):
    def __init__(self):
        self.parachute="   _____ \n"+"  /_____\ \n"+"  \     / \n"+"   \   / "
        self.skydiver="     0 \n"+"    /|\ \n"+"    / \ "
        get_word=Guesser()
        self._word=""
        self._word=get_word.get_word_with_placeholders()
        self.letters=get_word.get_random_word()

    def blast_parachute(self):
        skydiver ="     0 \n"+"    /|\ \n"+"    / \ "
        # removes a line from the jumper
        # n=0
        # while n != 5: 
        if self._word not in self.letters:
            parachute=self.parachute[10:]
            return parachute+skydiver
        # if n >= 4:
            skydiver=skydiver.replace("     0 \n","     X \n")
            print(skydiver)
            print("gameover")
        return parachute+skydiver

    def parachute_is_safe(self,word):

        for letter in word:
            if letter.lower() == True:
                print(letter,end= " ")
            else:
                print("_",end=" ") 
    
    def get_word_with_spaces(self):
        if Guesser == True:
            print(self._word_with_placeholders + self.letters)

    def get_jumper(self):
        return self.parachute +"\n"+ self.skydiver