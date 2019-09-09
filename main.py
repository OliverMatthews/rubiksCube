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
    user.getCube()
    user.instructions()
elif userInput == 2:
    numberOfSimulations = int(input("How many simulations would you like to run? "))
    dev.runSimulations(numberOfSimulations)
