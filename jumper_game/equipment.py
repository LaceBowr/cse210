
class Equipment(object):
    def __init__(self):
        self.jumper_details = [[' ',' ','_','_','_'],
            [' ','/','_','_','_','\\'],
            [' ','\\',' ',' ',' ','/'],
            [' ',' ','\\',' ','/',],
            [' ',' ',' ','0'],
            [' ',' ','/','|','\\'],
            [' ',' ','/',' ','\\ ',' ',' ',]]

    def blast_parachute(self):
        # TODO
        # removes a line from the jumper
        pass
    
    def get_jumper(self):
        return self.jumper_details