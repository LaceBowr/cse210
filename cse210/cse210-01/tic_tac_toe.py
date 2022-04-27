#Laycie Bowers
#W02 Prove: Developer - Solo code Submission
#CSE-210 -Section 10
import random

start_game = " "
player1 = "X"
computerPlayers = "N"
random_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
diagram_details = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

# How you assign a move to the board
def print_diagram():
    print(f'{diagram_details[0]}|{diagram_details[1]}|{diagram_details[2]}')
    print(f'-+-+-')
    print(f'{diagram_details[3]}|{diagram_details[4]}|{diagram_details[5]}')
    print(f'-+-+-')
    print(f'{diagram_details[6]}|{diagram_details[7]}|{diagram_details[8]}')

def get_move_player(symbol):
    while True:
        player_move = input(
        "Okay, Player #1! At what NUMBER would you like to put your X?\n\
        1|2|3\n\
        -+-+-\n\
        4|5|6\n\
        -+-+-\n\
        7|8|9")
        player_move = int(player_move)
        if diagram_details[player_move-1] == ' ':
            diagram_details[player_move-1] = symbol
            return
        else:
            print('Unavailable #. Please try again')

def get_move_computer(symbol):
    
    while True:
        move = random.choice(random_num)
        if diagram_details[move-1] == ' ':
            diagram_details[move-1] = symbol
            return

def check_for_winner():
    winner = False
    winning_symbol = " "
    if ((diagram_details[0]==diagram_details[4]==diagram_details[8]) and (diagram_details[0]=="X" or diagram_details[0]=="O")):
        print(f"{diagram_details[0]} HAS WON!")
        print_diagram()
        exit()
    elif (diagram_details[2]==diagram_details[4]==diagram_details[6] and (diagram_details[2]=="X" or diagram_details[2]=="O")):
        print(f"{diagram_details[2]} HAS WON!")
        print_diagram()
        exit()
    elif (diagram_details[6]==diagram_details[7]==diagram_details[8] and (diagram_details[6]=="X" or diagram_details[6]=="O")):
        print(f"{diagram_details[6]} HAS WON!")
        print_diagram()
        exit()
    elif (diagram_details[0]==diagram_details[1]==diagram_details[2] and (diagram_details[0]=="X" or diagram_details[0]=="O")):
        print(f"{diagram_details[0]} HAS WON!")
        print_diagram()
        exit()
    elif (diagram_details[3]==diagram_details[4]==diagram_details[5] and (diagram_details[3]=="X" or diagram_details[3]=="O")):
        print(f"{diagram_details[3]} HAS WON!")
        exit()    
    elif (diagram_details[0]==diagram_details[3]==diagram_details[6] and (diagram_details[0]=="X" or diagram_details[0]=="O")):
        print(f"{diagram_details[0]} HAS WON!")
        print_diagram()
        exit()
    elif (diagram_details[1]==diagram_details[4]==diagram_details[7] and (diagram_details[1]=="X" or diagram_details[1]=="O")):
        print(f"{diagram_details[1]} HAS WON!")
        exit()
    elif (diagram_details[2]==diagram_details[5]==diagram_details[8] and (diagram_details[2]=="X" or diagram_details[2]=="O")):
        print(f"{diagram_details[2]} HAS WON!")
        print_diagram()
        exit()
    else: 
        return
        
#draw = false if there is a NO draw
def check_for_draw():
    for item in diagram_details:
        if item == " ":
            return False
    print_diagram()
    print(f'No winners - It is a DRAW!')
    exit()


def main():
    # Prompt the user for a game of tic-tac-toe.
    start_game = input("Welcome to our game que! We will use the following diagram for your x's and O's move:\n\
        1|2|3\n\
        -+-+-\n\
        4|5|6\n\
        -+-+-\n\
        7|8|9\n\
        would you like to play Game que Tic-Tac-Toe? y=yes/n=no\n")
   
# Game GOES and prompts player 1 for entering an x.
    if start_game == "y":
        print("Okay Player #1 goes first, then Computer Player. Lets start!")
    else:
        print("Okay, Have a good day and hope you will\nplay Tic-Tac-Toe Game que in the future!")
        exit()
    

    while True:
        print_diagram()
        get_move_player('X')
        check_for_winner()
        check_for_draw()
        if computerPlayers:
            get_move_computer('O')
        else:
            get_move_player('O')
        check_for_winner()
        check_for_draw()

main()