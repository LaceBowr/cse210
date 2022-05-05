import random

# TODO: Implement the Die class as follows...
# 1) Add the class declaration. Use the following class comment.
#A small cube with a different number of spots on each of its six sides.

class Hilo:
# 2) Create the class constructor. Use the following method comment.
    #Constructs a new instance of Die with a value and points attribute.
    def __init__(self):#Args:self (Die): An instance of Die.            
    #Attributes:
    
        #points (int): The number of points the die is worth.
        #self.points = 0
        #value (int): The number of spots on the side facing up. int==1<=6
        #self.value = -1

 
    
# 3) Create the roll(self) method. Use the following method comment.
    #Generates a new random value and calculates the points.
    #def guess(self):
    # The responsibility of rolling the die is to keep track the 5 random numbers between 1 and 6 and calculate the points for  
    #each roll. 
        #self.value = random.choice([1,2,3,4,5,6])
        #1 = 100 points
        #if self.value == 1:
        #    self.points = 100
        #5 = 50 points
        #elif self.value == 5:
        #    self.points = 50
        #else:
        #NO 5 or 1 rolled = game_over (0 points)
        #    self.points = 0
