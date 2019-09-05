"""
Rubix Cube Solver - User Cube Input(s)

v0.10 (alpha)
History available at github.com/OliverMatthews/rubiksCube/

Oli Matthews 2019
"""

def printLayout(colour):

    # Central colour of the side, as a full string.
    sideColour = ""
    topColour = ""

    # Assigns a full string label for the colour of the side.
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

    print("Align the cube so that the side with the " + sideColour + " centre faces you, and the side with the " + topColour + " faces up.")
    print("In the order indicated by the layout below, input the colours around the " + sideColour + " centre.")
    print("[1, 2, 3]")
    print("[4, " + colour + ", 5]")
    print("[6, 7, 8]")