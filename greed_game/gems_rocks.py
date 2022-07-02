from video_service import VideoService

class Gems_rocks(VideoService):
    '''This class set gems and rocks positions and adjusts lines to give them a moving effect
    
    Attributes:
        self.player_hit()
        self.get_rock_position()
        self.get_gem_position()
        self.falling_movement()'''

    score = 0
    x = 0
    y = 0
    
    def __init__(self):
        #gems and rocks are compared to the set_character_move to determine add-ends or subtarct-end
        #and then a tally is updated and pushed to the director service to be added to a total.
        pass

    def player_hit_rock(self, character_move):
        while self.get_rock_position() == character_move:
            self.score.append(-1)
            if self.score > 0:
                print('Ouch... minus 1!')
                return self.score

            else:
                self.score <= 0
                print('SORRY score below 0... GAME OVER')
                return self.score

    def player_hit_gem(self, get_gem_position, set_character_move):
        while get_gem_position == set_character_move('x',39):
            self.score.append(+1)
            if self.score > 0:
                print('Awesome +1 !')
            return self.score

    def get_rock_position(self):
        return [self.x, self.y]

    def get_gem_position(self):
        return [self.x, self.y]

    def falling_movement(self, draw_grid):
        rows = 'y' in self.draw_grid
        line = self.y == self.y in self.draw_grid
        for i in line (self.x and self.y):
            line[0,38].replace == (self.x, self.y+1)





    
        


