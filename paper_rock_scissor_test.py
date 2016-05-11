# Rock-paper-scissors project
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors" to numbers
# as follows:
#
# 0 - "rock"
# 1 - "paper"
# 2 - "scissors"
def number_to_name(comp_number):
    # TODO [2]: return a name for input comp_number
    if comp_number is 0:
        return "rock"
    if comp_number is 1:
        return "paper"
    if comp_number is 2:
        return "scissors"
        
def print_result(player_choice, comp_choice):

    if player_choice == "rock" and comp_choice == "scissors" or \
       player_choice == "scissors" and comp_choice == "paper" or \
       player_choice == "paper" and comp_choice == "rock":
        print "Player wins!"
    
    if player_choice == "scissors" and comp_choice == "rock" or \
       player_choice == "paper" and comp_choice == "scissors" or \
       player_choice == "rock" and comp_choice == "paper":
        print "Computer wins!"
    
    if player_choice == "scissors" and comp_choice == "scissors" or \
       player_choice == "paper" and comp_choice == "paper" or \
       player_choice == "rock" and comp_choice == "rock":
        print "Player and computer tie!"

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "Player chooses", player_choice
    # print "Matt figured out that player_number is: ", player_number
    # compute random guess for comp_number using random.randrange()
    print ""
    
    comp_number = random.randrange(0, 3)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # TODO [4] print out the message for computer's choice
    print "Computer chooses" , comp_choice
    # TODO [5] print out the result
    print_result(player_choice, comp_choice)
    

    
    
# Test your code
rpsls(player_choice="rock")
# rpsls(player_choice="paper")
# rpsls(player_choice="scissors")
