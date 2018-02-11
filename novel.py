#!/usr/bin/python3


import sys, random

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

#base values of stats for the character
base_atk_max = 10
base_def_max = 3
base_speed = 5
base_perception = 10
base_luck = 5
base_persuasion = 20
base_knowledge = 100




def show_location(description,options):
    ''' Displays the description, displays a list of options, accepts and returns user input '''
    print(description)
    count = 1
    for o in options:
        print('[' + str(count) + '] ' + o)
        count = count + 1
    print('[q] to quit')
    choice = input("What do you choose? ")
    if choice.lower() == 'q':
        quit()
    return choice

def start():
    #checks if first time here or not
    loopcheck = 0
    if loopcheck == 0:
        loopcheck = loopcheck + 1
        description = "Exposition: \n   You are a treasure hunter in the search of the fabled scripts. These scripts have the power to turn you into a god.\n" \
                      "After all of your travels and readings you have found that the locations of these scripts: the Vault of Xar.\n" \
                      "You've been there before, but was forced to turn away due to facing opponents that were too strong for you at the time.\n" \
                      "However, that was 6 years ago, you are much stronger than you were then. You decided to go back and perhaps try your luck.\n" \
                      "What happens next? Well it hasn't happened yet\n \n \n" \
                      "You find yourself at the Tomb's entrance. What do you do next?"
        options = ["You decide you care too much about your life to risk the dangers of the Vault and turn back","You decide to take a look around before going into the tomb.","You go into the vault."]
        option = show_location(description,options)
        if option == "1":
            print("Thanks for playing, maybe next time you'll be brave enough to choose one of the other choices!")
            finish()
        elif option == "2":
            pcheck1 = random.randint(base_perception,100)
            perception1()
        elif option == "3":
            tree()
        else:
            print("Please choose one of the options")
            start()


def perception1():
    if pcheck1 >= 95:
        print("After looking around you find a book titled \"The Art of Persuasion\"\nAfter reading through it, you feel like you've mastered the art of persuasion")
        base_persuasion = base_persuasion + 80


start()
