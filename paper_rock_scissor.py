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
    #         comp_number could be 0, 1, 2 either
    #         How can we determind who wins??
    #           If Player wins, print "Player wins!"
    #           If Computer wins, print "Computer wins!"
    #           If tie, print "Player and computer tie!"
    # player_number = 0 , 1, 2
    # comp_number = 0 , 1 ,2


    diff = player_number - comp_number
    if diff < 0:
        diff = diff + 3

    if diff == 1:
        print "Player wins!"
    if diff == 2:
        print "Computer wins!"
    if diff == 0:
        print "Player and computer tie!"
 
# def print_result(player_number, comp_number):
#     # TODO [3]: player_number could be 0, 1, 2
#     #           comp_number could be 0, 1, 2 either
#     #           How can we determind who wins??
#     #           If Player wins, print "Player wins!"
#     #           If Computer wins, print "Computer wins!"
#     #           If tie, print "Player and computer tie!"
#     # player_number = 0 , 1, 2
#     # comp_number = 0 , 1 ,2

#     if player_number == "rock" and comp_number == 2 or \
#        player_number == 2 and comp_number == 1 or \
#        player_number == 1 and comp_number == "rock":
#         print "Player wins!"
    
#     if player_number == 2 and comp_number == 0 or \
#        player_number == 1 and comp_number == 2 or \
#        player_number == 0 and comp_number == 1:
#         print "Computer wins!"
    
#     if player_number == 2 and comp_number == 2 or \
#        player_number == 1 and comp_number == 1 or \
#        player_number == 0 and comp_number == 0:
#         print "Player and computer tie!"

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "Player chooses", player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # print "Matt figured out that player_number is: ", player_number
    # compute random guess for comp_number using random.randrange()
    print ""
    
    comp_number = random.randrange(0, 3)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # TODO [4] print out the message for computer's choice
    print "Computer chooses" , comp_choice
    # TODO [5] print out the result
    print_result(player_number, comp_number)
    

    
    
# Test your code
rpsls(player_choice="rock")
# rpsls(player_choice="paper")
# rpsls(player_choice="scissors")
