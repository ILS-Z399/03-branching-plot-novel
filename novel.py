#!/usr/bin/python3


import sys, random

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'


class Novel:

    #base values of stats for the character
    def __init__(self):
        '''starting stats of the player, can be changed'''
        self.current_atk = 10
        self.current_def_max = 3
        self.current_perception = 10
        self.current_persuasion = 20
        self.current_health = 100
        self.enemy1_health = 30
        self.perception_check = 0
        self.persuasion_check = 0
        self.boss_health = 120

    def reset(self):
        '''resets the players stats'''
        self.current_atk = 10
        self.current_def_max = 3
        self.current_perception = 10
        self.current_persuasion = 20
        self.current_health = 100
        self.enemy1_health = 30
        self.perception_check = 0
        self.persuasion_check = 0
        self.boss_health = 120

    def alive(self):
        '''checks if the player is still alive'''
        if self.current_health > 0:
            pass
        else:
            print("You died! Better luck next time!")
            self.finish()

    def atk1(self):
        '''player attack enemy type 1'''
        self.enemy1_health = self.enemy1_health - self.current_atk
        print("You attack the enemy hitting them for " + str(self.current_atk) + " dmg .They have " + str(self.enemy1_health) + "health left.")

    def atkboss(self):
        '''player attack boss'''
        self.boss_health = self.boss_health - self.current_atk
        print("You attack the enemy hitting them for " + str(self.current_atk) + " dmg .They have " + str(self.boss_health) + "health left.")

    def enemy1atk(self):
        '''enemy type 1 attack'''
        x1 = (random.randint(1,10) - self.current_def_max)
        if x1 >= 0:
            pass
        if x1 < 0:
            x1 = 0
        self.current_health = self.current_health - x1
        self.alive()
        print("Enemy hit you for " + str(abs(x1)) + " You have " + str(self.current_health) + " health left.")

    def bossatk(self):
        '''boss attack'''
        x1 = (random.randint(20,50) - self.current_def_max)
        if x1 >= 0:
            pass
        if x1 < 0:
            x1 = 0
        self.current_health = self.current_health - x1
        self.alive()
        print("Enemy hit you for " + str(abs(x1)) + " You have " + str(self.current_health) + " health left.")

    def enemy1_alive_check(self):
        '''checks if the enemy is still alive'''
        if self.enemy1_health > 0:
            pass
        else:
            print("Your enemy has died.")
            self.enemy1_health = 30
            self.vault1c()

    def enemy2_alive_check(self):
        '''checks if the 2nd enemy is still alive'''
        if self.enemy1_health > 0:
            pass
        else:
            print("Your enemy has died.")
            self.enemy1_health = 30
            self.vault3d3()

    def boss_alive_check(self):
        '''checks if the boss is still alive'''
        if self.boss_health > 0:
            pass
        else:
            print("Your enemy has died.")
            self.boss_health = 120
            self.vault1c()

    def perception_roll(self):
        '''perception roll'''
        self.perception_check = random.randint(self.current_perception, 100)

        print(str(self.perception_check))

    def persuasion_roll(self):
        '''persuasion roll'''
        self.persuasion_check = random.randint(self.current_persuasion, 100)

        print(str(self.persuasion_check))

    def perception_fail(self):
        '''result of failing perception check'''
        print("After looking, you find nothing.")

    def validation(self):
        '''tells the user to choose a valid answer'''
        print("Please choose one of the options")

    def anti_reroll(self):
        '''text for preventing rerolling perception'''
        print("You're wasting time, do something else.")

    def persuasion_fail(self):
        '''text for failing persuasion check'''
        print("You're attempts at peace fail and they attack.")




    def show_location(self, description, options):
        ''' Displays the description, displays a list of options, accepts and returns user input '''
        print(description)
        for i, o in enumerate(options, start=1):
            print(f'[{i}] {o}')
        print('[q] to quit')
        choice = input("What do you choose? ")
        if choice.lower() == 'q':
            quit()
        return choice

    def begin(self):
        '''area 1'''
        description = "Exposition: \n   You are a treasure hunter in the search of the fabled scripts. These scripts have the power to turn you into a god.\n" \
                        "After all of your travels and readings you have found that the locations of these scripts: the Vault of Xar.\n" \
                        "You've been there before, but was forced to turn away due to facing opponents that were too strong for you at the time.\n" \
                        "However, that was 6 years ago, you are much stronger than you were then. You decided to go back and perhaps try your luck.\n" \
                        "What happens next? Well it hasn't happened yet\n \n \n" \
                        "You find yourself at the Vault's entrance. What do you do next?"
        options = ["You decide you care too much about your life to risk the dangers of the Vault and turn back","You decide to take a look around before going into the tomb.","You go into the vault."]
        option = self.show_location(description, options)
        if option == "1":
            self.finish()
        elif option == "2":
            self.perception_roll()
            self.perception1(self.perception_check)
        elif option == "3":
            self.vault1a()
        else:
            self.validation()
            self.begin()

    def start(self):
        '''area 1: perception choice anti reroll'''
        description = "You find yourself at the Vault's entrance. What do you do next?"
        options = ["You decide you care too much about your life to risk the dangers of the Vault and turn back","You decide to take a look around before going into the tomb.","You go into the vault."]
        option = self.show_location(description, options)
        if option == "1":
            self.finish()
        elif option == "2":
            self.anti_reroll()
            self.start()
        elif option == "3":
            self.vault1a()
        else:
            print("Please choose one of the options")
            self.start()

    def finish(self):
        '''ending'''
        description = "Thanks for playing!"
        options = ["Would you like to try again?"]
        option = self.show_location(description, options)
        if option == "1":
            self.reset()
            self.begin()

        else:
            print("Please choose one of the options")
            self.finish()

    def perception1(self, p):
        '''perception check for area 1'''
        if p >= 95:
            print("After looking around you find a book titled \"The Art of Persuasion\"\nAfter reading through it, you feel like you've mastered the art of persuasion")
            self.current_persuasion = self.current_persuasion + 80
            self.start()
        elif p < 95:
            self.perception_fail()
            self.start()

    def vault1a(self):
        '''area 2'''
        description = "You enter the tomb, before you step one foot in the entrance, You are met by one of its guards. \n" \
        "Judging by its stance, it's here to fight you."
        options = ["Persuade it to not fight you.", "Prepare to fight.", "Do nothing."]
        option = self.show_location(description, options)
        if option == "1":
            p1 = random.randint(self.current_persuasion, 100)
            if p1 > 80:
                print("You convince the guard to leave you alone and proceed into the vault")
                self.vault2()
            if p1 <= 80:
                print("Your attempts at peace fail, and the monster attacks you again.")
                self.enemy1atk()
                self.vault1b()
        elif option == "2":
            self.atk1()
            self.enemy1_alive_check()
            self.enemy1atk()
            self.vault1b()
        elif option == "3":
            self.enemy1atk()
            self.vault1b()
        else:
            self.validation()
            self.vault1a()

    def vault1b(self):
        '''area 2: combat'''
        description = "You are in combat with the guard."
        options = ["Make another attempt at persuading the guard to not fight you.", "Fight it.", "Do nothing."]
        option = self.show_location(description, options)
        if option == "1":
            p1 = random.randint(self.current_persuasion, 100)
            if p1 > 80:
                print("You convince the guard to leave you alone and proceed into the vault")
                self.vault2()
            if p1 <= 80:
                print("Your attempts at peace fail, and the monster attacks you again.")
                self.enemy1atk()
                self.vault1b()
        elif option == "2":
            self.atk1()
            self.enemy1_alive_check()
            self.enemy1atk()
            self.vault1b()

        elif option == "3":
            self.enemy1atk()
            self.vault1b()
        else:
            self.validation()
            self.vault1b()

    def vault1c(self):
        '''area 2: encounter passed'''
        description = "The guard is dead, what do you do?"
        options = ["Search the body", "Proceed further", "Do nothing"]
        option = self.show_location(description, options)
        if option == "1":
            self.perception_roll()
            self.perception2(self.perception_check)
        elif option == "2":
            self.vault2()
        elif option =="3":
            self.vault1c()
        else:
            self.validation()
            self.vault1c()

    def perception2(self, p):
        '''area 2: perception check'''
        if p >= 20:
            print("You find a scroll tucked in one of its pockets. It is about fighting and after reading through it, you feel as if you have a better grasp at combat.")
            self.current_atk = self.current_atk + 10
            self.vault1d()
        elif p < 20:
            self.perception_fail()
            self.vault1d()

    def vault1d(self):
        '''area 2: anti perception reroll'''
        description = "The guard is dead, what do you do?"
        options = ["Search the body", "Proceed further", "Do nothing"]
        option = self.show_location(description, options)
        if option == "1":
            self.anti_reroll()
            self.vault1d()
        elif option == "2":
            self.vault2()
        elif option == "3":
            self.vault1d()
        else:
            self.validation()
            self.vault1d()

    def vault2(self):
        '''area 3'''
        description = "You make your way into the vault. After some walking you come across a fork in the path. The path left \n " \
        "leads down a long staircase, upon close inspection, you notice that there are dried blood on the steps. \n" \
        "The path right leads up a staircase, upon inspecting that, you notice that you can hear a deep droning coming from above. What do you do?"
        options = ["Go left, down the staircase.", "Go right, up the staircase.", "Take a look around"]
        option = self.show_location(description, options)
        if option == "1":
            print("You go down the staircase")
            self.vault3d()
        elif option == "2":
            print ("You go up the staircase")
            self.vault3u()
        elif option == "3":
            self.perception_roll()
            self.perception3(self.perception_check)
        else:
            self.validation()
            self.vault2()

    def perception3(self, p):
        '''area 3: perception check'''
        if p >= 55:
            print("Upon closer inspection, you find that in between the 2 paths is a door.")
            self.vault2a()
        elif p <= 55:
            self.perception_fail()
            self.vault2b()

    def vault2a(self):
        '''area 3: perception check passed'''
        description = "What do you do?"
        options = ["Go left, down the staircase.", "Go right, up the staircase.", "Go through the door"]
        option = self.show_location(description, options)
        if option == "1":
            print("You go down the staircase, the door disappears")
            self.vault3d()
        elif option == "2":
            print ("You go up the staircase. Halfway up, you notice the steps have disappeared. No turning back")
            self.vault3u()
        elif option == "3":
            print("You go through the door")
            self.vaultf()
        else:
            self.validation()
            self.vault2a()

    def vault2b(self):
        '''area 3: anti perception reroll'''
        description = "What do you do?"
        options = ["Go left, down the staircase.", "Go right, up the staircase.", "Take a look around"]
        option = self.show_location(description, options)
        if option == "1":
            print("You go down the staircase")
            self.vault3d()
        elif option == "2":
            print ("You go up the staircase. Halfway up, you notice the steps have disappeared. No turning back")
            self.vault3u()
        elif option == "3":
            self.anti_reroll()
            self.vault2b()
        else:
            self.validation()
            self.vault2b()

    def vaultf(self):
        '''final area'''
        description = "You open the door and step into the room. In the center of the room, you see a pedestal. On the pedestal are some scripts, your heart starts racing as you realize those are *the* scripts \n" \
        "You stop thinking and run towards it. Before you can get there you are knocked down by a being of arcane power that has appeared out of nowhere. \n"
        "It says to you \"Leave now, and I will spare you. Stay and you shall die.\" What do you do?"
        options = ["Try to persuade the being to let you have the scripts freely.", "Fight the being.", "Take a look around.", "Do nothing."]
        option = self.show_location(description, options)
        if option == "1":
            self.persuasion_roll()
            self.persuasionf(self.persuasion_check)
        elif option == "2":
            self.atkboss()
            self.bossatk()
            self.vaultf1()
        elif option == "3" or "4":
            print("Before you can do anything, the being attacks you")
            self.bossatk()
            self.vaultf1()
        else:
            self.validation()
            self.vaultf()

    def persuasionf(self, p):
        '''boss persusaion check'''
        if p >= 100:
            print("You convince the being to let you pass.")
            self.vaultff()
        elif p < 100:
            self.persuasion_fail()
            self.bossatk()
            self.vaultf1()

    def vaultf1(self):
        '''final area: combat'''
        description = "You are in combat with the being what do you do?"
        options = ["Try to persuade the being to let you have the scripts freely.", "Fight the being.", "Take a look around.", "Do nothing."]
        option = self.show_location(description, options)
        if option == "1":
            self.persuasion_roll()
            self.persuasionf(self.persuasion_check)
        elif option == "2":
            self.atkboss()
            self.bossatk()
            self.vaultf1()
        elif option == "3" or "4":
            print("Before you can do anything, the being attacks you")
            self.bossatk()
            self.vaultf1()
        else:
            self.validation()
            self.vaultf()


    def vaultff(self):
        '''final area: encounter passed'''
        description = "At last you have the scripts. After reading them you are infused with the ability to become a immortal. \n" \
        "However, you also find that instead of becoming an immortal, you can go back to the start of your journey retaining all knowledge and stats. \n" \
        "You also find that you can go back to the start of your journey without forgetting everything, and losing the abilities you gained on the way."
        options = ["Become immortal (Ends game)", "Restart your journey, knowledge retained (New Game+)", "Restart your jorney, forgetting everything (New Game"]
        option = self.show_location(description, options)
        if option == "1":
            print("Thanks for playing")
        elif options == "2":
            self.begin()
        elif options == "3":
            self.reset()
            self.begin()

    def vault3d(self):
        '''area 4 down'''
        description = "You go down the steps. Once you reach the bottom you find yourself face to face with another guard. What do you do?"
        options = ["Go back up the stairs", "Fight the guard", "Try to persuade the guard to leave", "Take a look around", "Do nothing"]
        option = self.show_location(description, options)
        if option == "1":
            print("You hurry up the stairs")
            self.vault2b()
        elif option == "2":
            self.atk1()
            self.enemy2_alive_check()
            self.enemy1atk()
            self.vault3d1()
        elif option == "3":
            self.persuasion_roll()
            self.persuasion2(self.persuasion_check)
        elif option == "4":
            print("You can see a door behind the guard.")
            self.vault3d()
        elif option == "5":
            print("You do nothing.")
            self.vault3d1()

    def vault3d1(self):
        '''area 4 down: combat'''
        description = "You are in combat with the guard."
        options = ["Make another attempt at persuading the guard to not fight you.", "Fight it.", "Do nothing.", "Go back up the stairs"]
        option = self.show_location(description, options)
        if option == "1":
            self.persuasion_roll()
            self.persuasion2(self.persuasion_check)
        elif option == "2":
            self.atk1()
            self.enemy2_alive_check()
            self.enemy1atk()
            self.vault3d1()

        elif option == "3":
            self.enemy1atk()
            self.vault3d1()
        elif option == "4":
            self.vault2b()
        else:
            self.validation()
            self.vault3d1()

    def persuasion2(self, u):
        '''area 4 down: persuasion check'''
        if u >= 80:
            print("You convince the guard to let you pass.")
            self.vault3d2()
        elif u < 80:
            self.persuasion_fail()
            self.enemy1atk()
            self.vault3d1()

    def vault3d3(self):
        '''area 4 down: encounter passed'''
        description = "The guard is dead. What do you do?"
        options = ["Search the body", "Proceed through the door", "Do nothing", "Go back up the stairs"]
        option = self.show_location(description, options)
        if option == "1":
            self.perception_roll()
            self.perception4(self.perception_check)
        elif option == "2":
            self.vaultf()
        elif option == "3":
            self.vault3d3()
        elif option == "4":
            print("As you head up the stairs, you look back behind you and notice that a new guard has appeared.")
            self.vault2b()
        else:
            self.validation()
            self.vault3d3()

    def perception4(self, p):
        '''area 4 down: perception check'''
        if p >= 20:
            print("You find that the guard is equipped with a huge sword and take it")
            self.current_atk = self.current_atk + 40
            self.vault3d2()
        elif p < 20:
            print("You find nothing")
            self.vault3d2()

    def vault3d2(self):
        '''area 4 down: perception check passed'''
        description = "You are face to face with a door. What do you do?"
        options = ["Proceed through the door", "Do nothing", "Go back up the stairs"]
        option = self.show_location(description, options)
        if option == "1":
            self.vaultf()
        elif option == "2":
            print("You do nothing.")
            self.vault3d2()
        elif option == "3":
            print("As you head up the stairs, you look back behind you and notice that the guard has returned")
        else:
            self.validation()
            self.vault3d2()

    def vault3u(self):
        '''area 4 up'''
        description = "You find yourself in a room. You see that there is a door at the other end of the room and to the side you see a set of armor."
        options = ["Take a look around", "Go through the door", "Put on the armor", "Do nothing"]
        option = self.show_location(description, options)
        if option == "1":
            print("As you start to look around, the armor stand disappears.")
            self.perception_roll()
            self.perception6(self.perception_check)
        elif option == "2":
            self.vaultf()
        elif option == "3":
            "Print you put on the armor. It is surprisingly light. After putting it on the armor stand disappears."
            self.current_def_max = self.current_def_max + 20
            self.vault3u1()
        elif option == "4":
            self.vault3u()

        else:
            self.validation()
            self.vault3u()
    def perception6(self, p):
        '''area 4 up perception check'''
        if p >= 40:
            print("You find a sword hidden in the back corner of the room")
            self.current_atk = self.current_atk + 20
        if p < 40:
            print("After searching you find nothing")
        self.vault3u2()

    def vault3u1(self):
        '''area 4 up: armor taken'''
        description = "You find yourself in the room. There is a door at the end of the room"
        options = ["Take a look around", "Go through the door", "Do nothing"]
        option = self.show_location(description, options)
        if option == "1":
            self.perception_roll()
            self.perception6(self.perception_check)
        elif option == "2":
            self.vaultf()
        elif option == "3":
            self.vault3u1()
        else:
            self.validation()
            self.vault3u1()

    def vault3u2(self):
        '''area 4 up: perception done'''
        description = "You find yourself in the room. There is a door at the end of the room"
        options = ["Take a look around", "Go through the door", "Do nothing"]
        option = self.show_location(description, options)
        if option == "1":
            self.anti_reroll()
            self.vault3u2()
        elif option == "2":
            self.vaultf()
        elif option == "3":
            self.vault3u2()
        else:
            self.validation()
            self.vault3u2()

if __name__ == '__main__':
    novel = Novel()
    novel.begin()