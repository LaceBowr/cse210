import random

class Guesser:
    """The person guessing letters in the word selected from the computer at random. 

    The responsibility of Guesser is to collect input and validate if guesses are RIGHT or WRONG. 

    Attributes:
        check_guess (True=RIGHT or False=WRONG): The letter selected between (A-Z).
        _random_word (auto_generated): The letters that can end up correctly guessed.
    """

    def __init__(self):
        """Constructs a new Guess.

        Args:
            self (Guess): A new instance of Jumper.
        """
        # the random word we will be guessing
        self._random_word = ""

        # The current guessed state of the random word above
        # for testing I have set it to random half guessed word
        self._word_with_placeholders = "A_la__"

    # A random word is generated and stores it in the guesser class that will be used thoughout the game.
    def random_word(self):
        # TODO
        return

    def check_guess(self, player_move):
        # TODO
        # checks the player_move and returns true if it is in the word, false otherwise.
        # and updates the current state of _word_with_placeholders
        return True

    def get_word_with_placeholders(self):
        return self._word_with_placeholders