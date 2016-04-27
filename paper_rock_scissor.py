# Rock-paper-scissors project
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors" to numbers
# as follows:
#
# 0 - "rock"
# 1 - "paper"
# 2 - "scissors"

# helper functions
# Hint:
# 1) check comparision
#    if name is "rock":      means if a equal to b
# 2) remember to return value by:
#    return XXXXX
# 3) name_to_number("rock")

def name_to_number(player_choice):
    # TODO [1]: return a number for input player_choice
    if player_choice is "rock":
        return 0
    if player_choice is "paper":
        return 1
    if player_choice is "scissors":
        return 2

def number_to_name(comp_number):
    # TODO [2]: return a name for input comp_number
    if comp_number is 0:
        return "rock"
    if comp_number is 1:
        return "paper"
    if comp_number is 2:
        return "scissors"

def print_result(player_number, comp_number):
    # TODO [3]: player_number could be 0, 1, 2
    #			comp_number could be 0, 1, 2 either
    #			How can we determind who wins??
    #           If Player wins, print "Player wins!"
    #           If Computer wins, print "Computer wins!"
    #           If tie, print "Player and computer tie!"
    print "I need to print out the result here !"
    
def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "Player chooses", player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 2)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print_result(player_number, comp_number)
    

    
    
# Test your code
rpsls(player_choice="rock")
rpsls(player_choice="paper")
rpsls(player_choice="scissors")
