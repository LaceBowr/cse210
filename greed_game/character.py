import pyray
from position import Position
from gems_rocks import Gems_rocks
score = 0
class Character(Position, Gems_rocks):

    def __init__(self):
        self.character_score=[]
        self.dx = 0 
        self.dy = 0

    def get_character_move(self, direction):
        self.dx = direction[0]
        self.dy = direction[1]
        move = self.dx * pyray.is_key_down(pyray.KEY_LEFT) or self.dx * pyray.is_key_down(pyray.KEY_RIGHT)
        self.dx =  + move
        self.dy = 39
        return self.dx,self.dy
        
    def character_score(self,player_hit_gem, player_hit_rock):
        g_r= Gems_rocks
        while (g_r.player_hit_gem or g_r.player_hit_rock):
            if g_r.player_hit_gem:
                self.score += 1
            return self.score
            
        else:
            self.score -= 1
            return self.score

    