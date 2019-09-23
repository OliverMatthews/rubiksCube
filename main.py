"""
Rubix Cube Solver - Main Script

v0.11 (alpha)
History available at github.com/OliverMatthews/rubiksCube/

Oli Matthews 2019
"""
# Imports relevant libraries.
import dev
import user

# This function serves as the main menu for the program. It gives the user a
# list of options for what they would like to do with the program. Takes no
# inputs, and returns a boolean.
def mainMenu():
    # Prints a list of options for the user.
    print("\n" + "*** RUBIK'S CUBE SOLVER - MAIN MENU ***")
    print("Please choose from the following options:")
    print("1 - Solve a specific cube.")
    print("2 - (DEVELOPER) Run simulations.")
    print("3 - (DEVELOPER) Change developer settings.")
    print("0 - Exit.")
    # Asks for the user's selection.
    userInput = int(input(""))

    # If user opts to solve a specific cube.
    if userInput == 1:
        # Repeats the menu option repeatedly until the user selects to return
        # to the main menu.
        menuBool = True
        while menuBool == True:
            menuBool = option1()
        
        # Returns true, to loop back to the main menu again.
        return True

    # If user opts to run simulations.
    elif userInput == 2:
        # Repeats the menu option repeatedly until the user selects to return
        # to the main menu.
        menuBool = True
        while menuBool == True:
            menuBool = option2()
        
        # Returns true, to loop back to the main menu again.
        return True
    
    # If user opts to change settings.
    elif userInput == 3:
        # Repeats the menu option repeatedlt until the user selects to return
        # to the main menu.
        menuBool = True
        while menuBool == True:
            menuBool = option3()

        # Returns true, to loop back to the main menu again.
        return True
    
    # If user opts to exit the program.
    elif userInput == 0:
        print("See you soon! :)")

        # Returns false, to exit the loop and end the program.
        return False

    # If the user makes an invalid selection.
    else:
        print("That selection was not recognised.")

        # Returns true, to loop back to the main menu again.
        return True

# Asks the user for the state of their cube, then solves it, and prints out
# a list of instructions for the user to follow.
def option1():
    # Gets the state of the cube from the user.
    user.getCube()

    # Prints out instructions for the user to follow.
    user.instructions()

    # Loop to ask the user if they would like to solve another cube or return
    # to the main menu.
    while True:
        print("Would you like to solve another cube?")
        print("1 - Solve another cube")
        print("0 - Return to main menu")
        userInput = int(input(""))

        # If the user opts to return to the main menu.
        if userInput == 0:
            # Returns false to break the main menu loop.
            return False
            break

        # If the user opts to solve another cube.
        elif userInput == 1:
            # Returns true to maintain the main menu loop.
            return True
            break

        # If the user makes an invalid selection.
        else:
            print("That selection was not recognised.")
            continue

# This function is run if the user opts to run simulations. It asks the user
# how many simulations they would like to run (and checks that it is a sensible
# number), then runs them.
def option2():
    # Asks the user how many simulations they would like to run.
    numberOfSimulations = int(input("How many simulations would you like to run? "))

    # Checks the number of simulations to see how large the number is. This
    # check exists to ensure the user does not accidentally input a very large
    # number which will take an exceptionally long time to complete.
    if numberOfSimulations <= 10000:
        # Runs the simulations without checking if the number of simulation is
        # less than 10 000.
        dev.runSimulations(numberOfSimulations)
    elif numberOfSimulations > 10000:
        # Queries the user if they meant to input such a large number of
        # simulations. User is required to input the same number in again, to
        # confirm,
        print("WARNING: Running this many simulations may take a significant amount of time. Please enter the same number of simulations again to confirm.")
        confirmationNumberOfSimulations = int(input("Confirm number of simulations: "))

        # Checks the confirmation number against the original number of
        # simulations.
        if confirmationNumberOfSimulations == numberOfSimulations:
            # If the numbers match, runs the desired number of simulations.
            dev.runSimulations(numberOfSimulations)
        else:
            # If the numbers do not match, cancels running the simulations.
            print("Inputs did not match - running simulations cancelled.")

    # Loops the following submenu until a valid selection is made.
    while True:
        # Prints a list of options for the user.
        print("Would you like to run more simulations?")
        print("1 - Run more simulations")
        print("0 - Return to main menu")
        userInput = int(input(""))
        
        # If the user opts to return to the main menu.
        if userInput == 0:
            return False
            break

        # If the user opts to run more simulations.
        elif userInput == 1:
            return True
            break

        # If the user makes an invalid selection.
        else:
            print("That selection was not recognised.")
            continue
    
# This function is run if the user opts to change the developer settings.
# A sub-menu is provided to ask the user which setting(s) they wish to alter.
def option3():
    # Prints a list of options for the user.
    print("Please select a developer setting to change from the list below:")
    print("1 - Sequence Printing")
    print("2 - Simulation pass/fail statistics printing")
    print("3 - Simulation estimated time remaining status printing")
    print("4 - Simulation final time statistics printing")
    print("5 - Solution Saving")
    userInput = int(input(""))

    # Runs whichever selection the user makes.
    if userInput == 1:
        option3_1()
    elif userInput == 2:
        option3_2()
    elif userInput == 3:
        option3_3()
    elif userInput == 4:
        option3_4()
    elif userInput == 5:
        option3_5()
    # If the user makes an invalid selection, prints that the selection was
    # not recognised.
    else:
        print("That selection was not recognised.")

    # Loops the following submenu until a valid selection is made.
    while True:
        print("Would you like to change other settings?")
        print("1 - Change more settings")
        print("0 - Return to main menu")
        userInput = int(input(""))

        # Runs whichever selection the user makes.
        if userInput == 0:
            return False
            break
        elif userInput == 1:
            return True
            break
        # If the user makes an invalid selection, prints that the selection
        # was not recognised.
        else:
            print("That selection was not recognised.")
            continue

# This function is run if the user opts to change the state of the sequence
# printing setting. A sub-menu is provided to ask the user whether they
# wish to enable or disable sequence printing.
def option3_1():
    # Prints a list of options for the user.
    print("Please choose whether to enable or disable Sequence Printing.")
    print("1 - Enable (turn ON sequence printing)")
    print("2 - Disable (turn OFF sequence printing)")
    userInput = int(input(""))

    # Runs whichever selection the user makes.
    if userInput == 1:
        option3_1_1()
    elif userInput == 2:
        option3_1_2()
    # If the user makes an invalid selection, prints that the selection was
    # not recognised.
    else:
        print("That selection was not recognised.")

# This function is run if the user opts to enable sequence printing.
def option3_1_1():
    dev.devSettings.toggleSequencePrinting(True)

# This function is run if the user opts to disable sequence printing.
def option3_1_2():
    dev.devSettings.toggleSequencePrinting(False)

# This function is run if the user opts to change the state of the simulation
# pass/fail statistics printing setting. A sub-menu is provided to ask the user
# whether they wish to enable or disable simulation pass/fail statistics
# printing.
def option3_2():
    # Prints a list of options for the user.
    print("Please choose whether to enable or disable simulation pass/fail statistics printing")
    print("1 - Enable (turn ON simulation pass/fail statistics printing)")
    print("2 - Disable (turn OFF simulation pass/fail statistics printing)")
    userInput = int(input(""))

    # Runs whichever selection the user makes.
    if userInput == 1:
        option3_2_1()
    elif userInput == 2:
        option3_2_2()
    # If the user makes an invalid selection, prints that the selection was
    # not recognised.
    else:
        print("That selection was not recognised.")

# This function is run if the user opts to enable simulation pass/fail
# statistics printing.
def option3_2_1():
    dev.devSettings.toggleSimFailStatsPrinting(True)

# This function is run if the user opts to disable simulation pass/fail
# statistics printing.
def option3_2_2():
    dev.devSettings.toggleSimFailStatsPrinting(False)

# This function is run if the user opts to change the state of the simulation
# estimated time remaining status printing setting. A sub-menu is provided to
# ask the user whether they wish to enable or disable simulation estimated time
# remaining status printing.
def option3_3():
    # Prints a list of options for the user.
    print("Please choose whether to enable or disable simulation estimated time remaining status printing")
    print("1 - Enable (turn ON simulation estimated time remaining status printing)")
    print("2 - Disable (turn OFF simulation estimated time remaining status printing)")
    userInput = int(input(""))

    # Runs whichever selection the user makes.
    if userInput == 1:
        option3_3_1()
    elif userInput == 2:
        option3_3_2()
    # If the user makes an invalid selection, prints that the selection was
    # not recognised.
    else:
        print("That selection was not recognised.")

# This function is run if the user opts to enable simulation estimated time
# remaining status printing.
def option3_3_1():
    dev.devSettings.toggleSimTimeStatusPrinting(True)

# This function is run if the user opts to disable simulation estimated time
# remaining status printing.
def option3_3_2():
    dev.devSettings.toggleSimTimeStatusPrinting(False)

# This function is run if the user opts to change the state of the simulation
# final time statistics printing setting. A sub-menu is provided to ask the
# user whether they wish to enable or disable the simulation final time
# statistics printing setting.
def option3_4():
    # Prints a list of options for the user.
    print("Please choose whether to enable or disable simulation final time statistics printing")
    print("1 - Enable (turn ON simulation final time statistics printing)")
    print("2 - Disable (turn OFF simulation final time statistics printing)")
    userInput = int(input(""))

    # Runs whichever selection the user makes.
    if userInput == 1:
        option3_4_1()
    elif userInput == 2:
        option3_4_2()
    # If the user makes an invalid selection, prints that the selection was not
    # recognised.
    else:
        print("That selection was not recognised.")
    
# This function is run if the user opts to enable simulation final time
# statistics printing.
def option3_4_1():
    dev.devSettings.toggleFinalTimeStatsPrinting(True)

# This function is run if the user opts to disable simulation final time
# statistics printing.
def option3_4_2():
    dev.devSettings.toggleFinalTimeStatsPrinting(False)

# This function is run if the user opts to change the state of the solution
# saving setting. A sub-menu is provided to ask the user whether they wish to
# enable or disable the solution saving setting.
def option3_5():
    # Prints a list of options for the user.
    print("Please choose whether to enable or disable solution saving")
    print("1 - Enable (turn ON solution saving)")
    print("2 - Disable (turn OFF solution saving)")
    userInput = int(input(""))

    # Runs whichever selection the user makes.
    if userInput == 1:
        option3_5_1()
    elif userInput == 2:
        option3_5_2()
    # If the user makes an invalid selection, prints that the selection was not
    # recognised.
    else:
        print("That selection was not recognised.")

# This function is run if the user opts to enable the saving solutions setting.
def option3_5_1():
    dev.devSettings.toggleSaveSolutions(True)

# This function is run if the user opts to disable the saving solutions
# setting.
def option3_5_2():
    dev.devSettings.toggleSaveSolutions(False)

# Loops running the main menu until the user opts to exit the program.
menuBool = True
while menuBool == True:
    # Runs the main menu function. All options in the main menu return true
    # to continue running the loop, with the exception of the option to exit,
    # which returns false and ends execution of the program.
    menuBool = mainMenu()