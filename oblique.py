import random
import strategies

quit_var = True  #track whether the user has quit

# pick and print the strategies
def strategy_picker():
    picker = random.randint(0, 27)
    print(strategies.sayings[picker])


# Basically the main "game loop"
while (quit_var == True):
    quit_letter = input("Press enter for another strategy, or enter q to quit\n")

    if (quit_letter == "q"):
        quit_var = False
    else:    
        strategy_picker()
