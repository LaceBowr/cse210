#from character import Character
#from keyboard_services import KeyboardService
import pyray
from keyboard_services import KeyboardService
from character import Character
from video_service import VideoService
from symbols import Symbols
from time import sleep

class Director():
    #Keeps track of input, updates, and output and sends them to their needed locations
    '''
    self.update_score
    self.get_input
    self.
    '''
    def __init__(self):
        self.score = 0
        #self.get_input=(int('x'))
        #self.output 

    def update_score(self):
        # TODO: evaluate symbols and determine if player has been 
        # hit by a rock or gem, then adjust the score.
        pass
        #Character.character_score += self.update_score()

    def get_input(self):
        question = input('Experience the thrill having gems or rocks fall upon you! <i>Greed</i>\nmight seem easy, but even the best treasure-hunter can end up in the wrong place and \nget hit by rocks.\nThe rules are simple.\n The character can move\non the screen trying to dodge or hit the falling objects.\n*If your character(#) move connects with a gem(*) you get a +1 to your score.\n*If the character move connects with a rock you get a -1 to your score.\n\nDo you want to start playing? y/n: ')   
        if question != "y":
            exit()
    
    def game_running(self):
        # TODO: determine when the game should stop, did the player win or lose?
        return True
    
    def falling_movement(self, symbols):
        # go through and adjust the y position of every item in the symbol list
        for symbol in symbols.symbols:
            if symbol.y < 39:
                symbol.y += 1
            else:
                symbol.y = 0

    def start_game(self):    
        # Demonstrate functional video service
        self.get_input()
        vs=VideoService()
        vs.open_window()
        symbols = Symbols() #KeyboardService.dx,KeyboardService.dy,(0,0,255,100),'#', False, player=True)
        ks = KeyboardService()
        while self.game_running():
            vs.draw_grid(symbols)
            playerx,playery = ks.get_direction()
            symbols.update_player_position(playerx,playery)
            self.falling_movement(symbols)
            sleep(1)            
            self.update_score()
        vs.close_window()
        