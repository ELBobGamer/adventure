import time
import random 

total_score = 0
weapon_taken = False

def print_pause(x):
    print(x)
    time.sleep(2)

# welcome messages
def start():
    global monsters, weapons
    print_pause("You are a brave adventurer")
    print_pause("who has been traveling through the forest for days.")
    print_pause("As you walk along the path")
    print_pause("you come across a fork in the road.")
    print_pause("To the left, you see a cave.")
    print_pause("To the right, you see a cottage")
    print("")
    print("Enter 1 to go to the cave")
    print("Enter 2 to go to the cottage")
    print("Where would you like to go?")
    monsters = random.choice(["dragon", "zombie", "medusa", "troll"])
    weapons = random.choice (["sword", "knife", "spear", "pistol"])

# reset all variables
def restart():
    global weapon_taken, total_score
    weapon_taken = False 
    total_score = 0
    start()

def play_again():
    while True:
        choice = input("Do you want to play again? y/n ")
        if choice.lower() == "y":
            restart()
            break
        elif choice.lower() == "n":
            print("Thanks for playing!")
            exit()
        else:
            print("(Please enter y or n)")

# win and lose conditions (score)
def check_score(): 
    if total_score >= 15:
        print("You win! Congratulations!") 
        play_again()
    elif total_score <= 0:
        print("You lose! Better luck next time.")
        play_again() 

def cave():
    global weapon_taken, total_score
    if weapon_taken:
        print_pause("You have entered this cave before.")
        print_pause("You explored it all and now it's empty")
    else:
        print_pause("You entered the cave.")
        print_pause("It's a small cave.")
        print_pause("You exploring it to find anything could help you.")
        print_pause("You found a chest.")
        print_pause(f"You opened it and found a {weapons}.")
        print_pause("You took it and left the cave")
        total_score += 10 
        print(f"Your score is: {total_score}")
        weapon_taken = True

def cottage():
    print_pause("You approach the cottage.")
    print_pause("You knocked the door.")
    print_pause(f"and found yourself standing in front of a {monsters}.")
    print_pause("That's scary!")
    print_pause("Would you fight him or run away ?")
    print("Enter 1 to fight him")
    print("Enter 2 to run away")

def back():
    print('Enter 1 to go to the cave')
    print('Enter 2 to go to the cottage')
    print('Where would you like to go?')

def fight():
    global weapon_taken, total_score
    if weapon_taken == True:
        print_pause(f"As the {monsters} tries to attack you")
        print_pause(f"You raise your {weapons} and killed him")
        print_pause(f"Congrats! You killed the {monsters}")
        total_score += 10
        print(f"Your score is: {total_score}")
    else:
        print_pause("You do your best...")
        print_pause("but you don't have any weapons.")
        print_pause(f"The {monsters} killed you")
        print_pause("Game Over!")
        total_score -= 10
        print(f"Your score is: {total_score}")

def run_away():
    global total_score
    print_pause("You run back into the fork.")
    print_pause("Don't panic, he doesn't follow you.")
    total_score -= 5
    print(f"Your score is: {total_score}")

start()

# game code
while True:
    choice1 = input("(Please enter 1 or 2)")
    if choice1 == "1":
        cave()
        check_score()
        back()
    elif choice1 == "2":
        cottage()
        choice2 = input("(Please enter 1 or 2)")
        if choice2 == "1":
            fight()
            check_score()
        elif choice2 == "2":
            run_away()
            check_score()
            back()
        else:
            print("invalid choice please enter 1 or 2")
    else:
        print("invalid choice please enter 1 or 2")
