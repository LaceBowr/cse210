

class InputAdministrator:
    """A service that handles terminal operations.
    
    The responsibility of a InputAdministrator is to provide input and output operations for the 
    terminal/jumper_game.
    """
    def __init__(self):
        pass
        jumper = parachute + skydiver + self._word_with_placeholders

    def display_jumper(self, jumper):
        '''Takes the jumper array and displays it to the screen in the current state'''
        print(jumper)
        #for line in jumper:
        #    print("".join(line))
            
    def text_for_input(self, prompt):
        """Gets alphabetical input from the terminal. Directs the user with the given prompt.

        Args: 
            self (InputAdministrator): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input (guess) as a letter suggested for the word.
        """
        return input(prompt)

    def text_results(self, text):
        ''' Display text to the screen '''
        print(text)