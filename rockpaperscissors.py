# Game of Rock-paper-scissors-lizard-spock
# The value of the strings is as follows

#0 Rock
#1 Spock
#2 Paper
#3 Lizard
#4 Scissors

import random
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "The number is out of range, try again!"
    
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Invalid name input!"
            

#Implementation of function game RPSLS

def rpsls(name):
    player_number = name_to_number(name)
    
    comp_number= random.randrange(0, 5)
    
    difference = (player_number - comp_number) % 5
    
    if difference == 0:
        result = "Player and computer tie!"
        
    elif difference == 1 or difference == 2:
        result = "Player wins!"
    else:
        result = "Computer wins!"
        
    comp_name = number_to_name(comp_number)
    
    print "Player chooses", name
    print "Computer chooses", comp_name
    print result
    if name != "scissors":
        print
        
        
#test
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")