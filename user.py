"""
Rubix Cube Solver - User Cube Input(s)

v0.10 (alpha)
History available at github.com/OliverMatthews/rubiksCube/

Oli Matthews 2019
"""
import solve

def printLayout(colour):

    # Central colour of the side, as a full string.
    sideColour = ""
    topColour = ""

    # Assigns a full string label for the colour of the side and the up face.
    if colour == "B":
        sideColour = "BLUE"
        topColour = "YELLOW"
    elif colour == "W":
        sideColour = "WHITE"
        topColour = "BLUE"
    elif colour == "R":
        sideColour = "RED"
        topColour = "BLUE"
    elif colour == "Y":
        sideColour = "YELLOW"
        topColour = "BLUE"
    elif colour == "O":
        sideColour = "ORANGE"
        topColour = "BLUE"
    elif colour == "G":
        sideColour = "GREEN"
        topColour = "WHITE"

    # Prints the layout for the user to follow using the full string labels.
    print("Align the cube so that the side with the " + sideColour + " centre faces you, and the side with the " + topColour + " faces up.")
    print("In the order indicated by the layout below, input the colours around the " + sideColour + " centre.")
    print("[1, 2, 3]")
    print("[4, " + colour + ", 5]")
    print("[6, 7, 8]")

def getInput(colour):

    # Asks the user for each of the 8 required inputs.
    colour1 = input("1: ")
    colour2 = input("2: ")
    colour3 = input("3: ")
    colour4 = input("4: ")
    colour5 = input("5: ")
    colour6 = input("6: ")
    colour7 = input("7: ")
    colour8 = input("8: ")

    # Merges the inputted colours into a side matrix.
    side = [[colour1, colour2, colour3], [colour4, colour, colour5], [colour6, colour7, colour8]]

    # Returns the complete side matrix as inputted by the user.
    return side

def getSide(colour):

    # Runs both the printLayout and getInput functions.
    printLayout(colour)
    side = getInput(colour)

    # Returns the complete side matrix as inputted by the user.
    return side

def getCube():

    # Runs the getSide function for each of the sides of the cube.
    solve.a.side1 = getSide("G")
    solve.a.side2 = getSide("W")
    solve.a.side3 = getSide("R")
    solve.a.side4 = getSide("Y")
    solve.a.side5 = getSide("O")
    solve.a.side6 = getSide("B")

def sequenceSpacer(sequence):

    spacedSequence = ""
    
    for i in range(int(len(sequence)/2)):
        spacedSequence = spacedSequence + str(sequence[0:2]) + ", "
        sequence = sequence[2:]

    return spacedSequence

def instructions():

    # Turns on saving cube solutions. This is required in order to have a log
    # of the sequence that was followed to complete the cube, so that the
    # sequence can later be given to the user.
    solve.cube.dev.devSettings.toggleSaveSolutions = True

    # Resets the sequence log to be blank.
    solve.a.sequenceLog = ""

    # Solves the whole cube.
    solve.totalSolve()

    # Prints the instructions for the user to follow.
    instructionsForUser = sequenceSpacer(solve.a.sequenceLog)
    print("There are " + str(int(len(solve.a.sequenceLog)/2)) + " moves needed to complete this cube.")
    print(instructionsForUser)