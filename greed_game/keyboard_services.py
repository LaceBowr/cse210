import pyray
class KeyboardService():
    '''Any keys pressed to move the cursor. Translates into movement.

        Attributes: self.get_direction()
                    self.set_direction()
                    
                Returns: selected direction'''
    dx = 30
    dy = 39   
    def __init__(self):
        '''Gets direction that the character implements and sends it to the Keyboard_service and Director.'''
        self.direction = self.new_direction()     

    def new_direction(self):
        #records the new changes made
        move = self.dx * pyray.is_key_down(pyray.KEY_LEFT) or self.dx * pyray.is_key_down(pyray.KEY_RIGHT)
        self.dx = 30 + move
        return self.dx,self.dy

    def get_direction(self):
        #takes input done by character in play and implements a move
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        dx,dy = self.new_direction() #= (dx,dy)
        #self.new_direction == get_direction(dx,dy) 
  
        return dx,dy

    def set_direction(self):
        #takes the get_direction coordinates and moves it to the Director starting 
        # the game with this input makes other functions complete by setting it to the screen 
        # in the video_service.  
        direction = input(f'continue? y/n')
        if direction == 'y':
            return True
        else:
            return False
