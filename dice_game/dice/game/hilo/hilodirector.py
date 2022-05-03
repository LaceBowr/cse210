from game.hilo import hilo
import random


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[points]): An accumulation or deduction of instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.hilo = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range():
            card = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13])  # constructor
            self.score.append(self.score)

    #def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        #while self.is_playing:
        #    self.get_inputs()
        #    self.do_updates()
        #    self.do_outputs()

    #def is_playing(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
    #    is_play = input("play Hilo? [y/n] ")
    #    self.is_playing = (random_card == "y")
       
    #def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
    #    if not self.is_playing:
    #        return 

    #    for i in range(len(self.dice)):
    #        die = self.dice[i]
    #        die.roll()
    #        self.score += die.points 
    #    self.total_score += self.score
        #you have to reset the self.score otherwise it will add in all the previous rolls too.  
        # this is why the total wasn't working properly at first
    #    self.score = 0

    #def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
    #    if not self.is_playing:
    #        return
        
    #    values = ""
    #    for i in range(len(self.dice)):
    #        die = self.dice[i]
    #        values += f"{die.value} "

    #    print(f"You rolled: {values}")
    #    print(f"Your score is: {self.total_score}\n")
    #    self.is_playing == (self.score > 0)