
from input_administrator import InputAdministrator
from guesser import Guesser
from equipment import Equipment
import random

class Director:
    """A pilot who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        start_game (boolean): Whether or not to keep playing.
        guesser (Guesser): The game's results of (wrong or right) guesses of letters.
        jumper_details(jumper): The Jumpers state in the game Dare-devil or Lucky-guy.
        InputAdministrator: For getting, keeping some information concealed, and displaying 
            information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._guesser = Guesser()
        self._input_administrator = InputAdministrator()
        self._equipment = Equipment()

    def check_for_winner(self):
        if "_" not in self._guesser.get_word_with_placeholders():
            return True
        else:
            return False

    def check_for_loser(self):
        if not self._equipment.parachute_is_safe():
            return True
        else:
            return False

   #How you get input and return the results to the screen:
    def start_game(self):
        # initialize the random word at the start of the game
        self._guesser.get_random_word()
        self._input_administrator.text_results("Okay, In jumper you first guess a letter in a word,\n" 
        "if your guess is RIGHT, it is printed in the spaces of the word below the jumper.\n"
        "if your guess is WRONG, one of the strings are cut from your jumpers parachute. OH NO!\n")
        while True:
            player_move = self._input_administrator.text_for_input("Please guess a letter between a-z:")
            #Deletes or blasts away one of the strings on the jumpers parachute
            if self._guesser.check_guess(player_move) != True:
                self._input_administrator.text_results("Incorrect")
                self._equipment.blast_parachute()
            self._input_administrator.text_results(self._guesser.get_word_with_placeholders())
            self._input_administrator.display_jumper(self._equipment.get_jumper())
            if self.check_for_loser() == True:
                self._input_administrator.text_results("You Lose")
                exit()
            if self.check_for_winner() == True:
                self._input_administrator.text_results("You Win!")

                exit()     

