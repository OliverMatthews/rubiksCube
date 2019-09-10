"""
Rubix Cube Solver - Main Script

v0.10 (alpha)
History available at github.com/OliverMatthews/rubiksCube/

Oli Matthews 2019
"""
# Imports relevant libraries.
import dev
import user

# Gives the user options on what they would like to do with the program.
print("Would you like to solve a specific cube, or run many simulations?")
print("1 - Solve a specific cube.")
print("2 - (DEVELOPER) Run simulations.")
userInput = int(input(""))

# Runs the users requests.
if userInput == 1:
    # Asks the user for the state of their cube, then solves it, and prints out
    # a list of instructions for the user to follow.
    user.getCube()
    user.instructions()
elif userInput == 2:
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
