# Rock-paper-scissors-lizard-Spock project
import random
 
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
 
# helper functions
 
def name_to_number(player_choice):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if player_choice == "rock":
        return 0
    elif player_choice == "Spock":
        return 1
    elif player_choice == "paper":
        return 2
    elif player_choice == "lizard":
        return 3
    elif player_choice == "scissors":
        return 4
    else:
        print "Invalid parameter for name_to_number", player_choice
 
def number_to_name(comp_number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if comp_number == 0:
        return "rock"
    elif comp_number == 1:
        return "Spock"
    elif comp_number == 2:
        return "paper"
    elif comp_number == 3:
        return "lizard"
    elif comp_number == 4:
        return "scissors"
    else:
        print "Invalid parameter for number_to_name", comp_number

# def print_result(player_number, comp_number):
#     if player_number == "rock" and comp_number == "rock":
#         print "Player and computer tie!"
#     elif player_number == "rock" and comp_number == "Spock":
#         print "Computer wins!"
#     elif player_number == "rock" and comp_number == "paper":
#         print "Computer wins!"
#     elif player_number == "rock" and comp_number == "lizard":
#         print "Player wins!"
#     elif player_number == "rock" and comp_number == "scissors":   
#         print "Player wins!"
    
#     elif player_number == "Spock" and comp_number == "rock":
#         print "Player wins!"
#     elif player_number == "Spock" and comp_number == "Spock":
#         print "Player and computer tie!"
#     elif player_number == "Spock" and comp_number == "paper":
#         print "Computer wins!"   
#     elif player_number == "Spock" and comp_number == "lizard":
#         print "Computer wins!"   
#     elif player_number == "Spock" and comp_number == "scissors": 
#         print "Player wins!"
    
#     elif player_number == "paper" and comp_number == "rock":
#         print "Player wins!"
#     elif player_number == "paper" and comp_number == "Spock": 
#         print "Player wins!"
#     elif player_number == "paper" and comp_number == "paper":
#         print "Player and computer tie!"   
#     elif player_number == "paper" and comp_number == "lizard":
#         print "Computer wins!"   
#     elif player_number == "paper" and comp_number == "scissors": 
#         print "Computer wins!"
    
#     elif player_number == "lizard" and comp_number == "rock":
#         print "Computer wins!"
#     elif player_number == "lizard" and comp_number == "Spock":
#         print "Player wins!"   
#     elif player_number == "lizard" and comp_number == "paper":
#         print "Player wins!" 
#     elif player_number == "lizard" and comp_number == "lizard":
#         print "Player and computer tie!"   
#     elif player_number == "lizard" and comp_number == "scissors": 
#         print "Computer wins!"
    
#     elif player_number == "scissors" and comp_number == "rock":
#         print "Computer wins!"
#     elif player_number == "scissors" and comp_number == "Spock":
#         print "Computer wins!"
#     elif player_number == "scissors" and comp_number == "paper":
#         print "Player wins!"   
#     elif player_number == "scissors" and comp_number == "lizard":
#         print "Player wins!"
#     elif player_number == "scissors" and comp_number == "scissors":
#         print "Player and computer tie!" 
       
def print_result(player_number, comp_number):       

    diff = player_number - comp_number
    if diff < 0:
        diff = diff + 5

    if diff == 1 or diff == 2:
        print "Player wins!"
    if diff == 3 or diff == 4:
        print "Computer wins!"
    if diff == 0:
        print "Player and computer tie!"

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "Player chooses", player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses", comp_choice
    # compute difference of comp_number and player_number modulo five
    print_result(player_number, comp_number)
    # diff = comp_number-player_number
    # if diff< 0: 
    #     diff += 5
    # if diff == 0:
    #     print "Player and computer tie!"
    # elif diff == 1 or diff == 2:
    #     print "Computer wins!"
    # elif diff == 3 or diff == 4:
    #     print "Player wins!"
     
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
 
# always remember to check your completed program against the grading rubric