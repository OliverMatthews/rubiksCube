"""
Rubix Cube Solver

v1.0 alpha

Oli Matthews 2018
"""
# Imports relevant libraries
from random import randint
import time
import datetime

# Shifts a given sequence of colours by an amount relevant to the size of the
# cube. Takes three inputs: cubeSize(integer), colourSequence(string) and
# inverse(bool).
def shiftColourSequence(cubeSize, colourSequence, inverse):
    # For a standard clockwise rotation, takes a side of colours and moves them
    # to the end of the sequence, then returns the altered sequence.
    if inverse == False:
        colourSequence = colourSequence[cubeSize:] + colourSequence[:cubeSize]
        return colourSequence
    
    # For an anticlockwise rotation, takes the last side of colours and moves
    # them to the start of the sequence, then returns the altered sequence.
    elif inverse == True:
        colourSequence = colourSequence[-cubeSize:] + colourSequence[:cubeSize]
        return colourSequence
    
# Uses matrix manipulation to rotate a side without changing the order of the
# colours in any way.
def rotateStillFace(side):
    
    # Code needs optimising - currently this calculates an anticlockwise
    # rotation of the face and just repeats it three times instead of rotating
    # clockwise.
    for i in range(3):
        for i in range(len(side)): 
            for j in range(i, len(side)): 
                temp = side[i][j] 
                side[i][j] = side[j][i] 
                side[j][i] = temp
            
        for i in range(len(side)): 
            j = 0
            k = len(side)-1
            while j < k: 
                temp = side[j][i] 
                side[j][i] = side[k][i] 
                side[k][i] = temp 
                j += 1
                k -= 1
        
    return side
    
# Rotates the 'left' face of the cube clockwise 90 degrees.
def rotateLeft(side1, side2, side6, side4, side5):
    colourSequence = ""
    
    for i in range(len(side1)-1, -1, -1):
        colourSequence = colourSequence + side1[i][0]
    
    for i in range(len(side2)-1, -1, -1):
        colourSequence = colourSequence + side2[i][0]
        
    for i in range(len(side6)-1, -1, -1):
        colourSequence = colourSequence + side6[i][0]
        
    for i in range(len(side4)):
        colourSequence = colourSequence + side4[i][2]
    
    colourSequence = shiftColourSequence(len(side1), colourSequence, False)
    
    for i in range(len(side1)-1, -1, -1):
        side1[i][0] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    for i in range(len(side2)-1, -1, -1):
        side2[i][0] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    for i in range(len(side6)-1, -1, -1):
        side6[i][0] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    for i in range(len(side4)):
        side4[i][2] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    side5 = rotateStillFace(side5)
            
    return side1, side2, side6, side4, side5

# Rotates the 'right' face of the cube clockwise 90 degrees.
def rotateRight(side1, side2, side6, side4, side3):
    colourSequence = ""
    
    for i in range(len(side6)):
        colourSequence = colourSequence + side6[i][2]
    
    for i in range(len(side2)):
        colourSequence = colourSequence + side2[i][2]
    
    for i in range(len(side1)):
        colourSequence = colourSequence + side1[i][2]
    
    for i in range(len(side4)-1, -1, -1):
        colourSequence = colourSequence + side4[i][0]
    
    colourSequence = shiftColourSequence(len(side1), colourSequence, False)
    
    for i in range(len(side6)):
        side6[i][2] = colourSequence[0]
        colourSequence = colourSequence[1:]
        
    for i in range(len(side2)):
        side2[i][2] = colourSequence[0]
        colourSequence = colourSequence[1:]
        
    for i in range(len(side1)):
        side1[i][2] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    for i in range(len(side4)-1, -1, -1):
        side4[i][0] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    side3 = rotateStillFace(side3)
    
    return side1, side2, side6, side4, side3

# Rotates the 'up' face of the cube clockwise 90 degrees.
def rotateUp(side2, side3, side4, side5, side6):
    colourSequence = ""
    
    for i in range(len(side2)):
        colourSequence = colourSequence + side2[0][i]
    
    for i in range(len(side3)):
        colourSequence = colourSequence + side3[0][i]
    
    for i in range(len(side4)):
        colourSequence = colourSequence + side4[0][i]
    
    for i in range(len(side5)):
        colourSequence = colourSequence + side5[0][i]
    
    colourSequence = shiftColourSequence(len(side2), colourSequence, False)
    
    for i in range(len(side2)):
        side2[0][i] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    for i in range(len(side3)):
        side3[0][i] = colourSequence[0]
        colourSequence = colourSequence[1:]
        
    for i in range(len(side4)):
        side4[0][i] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    for i in range(len(side5)):
        side5[0][i] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    side6 = rotateStillFace(side6)
    
    return side2, side3, side4, side5, side6

# Rotates the 'down' face of the cube clockwise 90 degrees.
def rotateDown(side2, side3, side4, side5, side1):
    colourSequence = ""
    
    for i in range(len(side2)-1, -1, -1):
        colourSequence = colourSequence + side2[2][i]
    
    for i in range(len(side5)-1, -1, -1):
        colourSequence = colourSequence + side5[2][i]
    
    for i in range(len(side4)-1, -1, -1):
        colourSequence = colourSequence + side4[2][i]
    
    for i in range(len(side3)-1, -1, -1):
        colourSequence = colourSequence + side3[2][i]
    
    colourSequence = shiftColourSequence(len(side2), colourSequence, False)
    
    for i in range(len(side2)-1, -1, -1):
        side2[2][i] = colourSequence[0]
        colourSequence = colourSequence[1:]
        
    for i in range(len(side2)-1, -1, -1):
        side5[2][i] = colourSequence[0]
        colourSequence = colourSequence[1:]
        
    for i in range(len(side2)-1, -1, -1):
        side4[2][i] = colourSequence[0]
        colourSequence = colourSequence[1:]
        
    for i in range(len(side2)-1, -1, -1):
        side3[2][i] = colourSequence[0]
        colourSequence = colourSequence[1:]
        
    side1 = rotateStillFace(side1)
    
    return side2, side3, side4, side5, side1

# Rotates the 'front' face of the cube clockwise 90 degrees.
def rotateFront(side1, side3, side6, side5, side2):
    colourSequence = ""
    
    for i in range(len(side1)):
        colourSequence = colourSequence + side1[0][i]
    
    for i in range(len(side3)-1, -1, -1):
        colourSequence = colourSequence + side3[i][0]
    
    for i in range(len(side6)-1, -1, -1):
        colourSequence = colourSequence + side6[2][i]
    
    for i in range(len(side5)):
        colourSequence = colourSequence + side5[i][2]
    
    colourSequence = shiftColourSequence(len(side1), colourSequence, False)
    
    for i in range(len(side1)):
        side1[0][i] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    for i in range(len(side3)-1, -1, -1):
        side3[i][0] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    for i in range(len(side6)-1, -1, -1):
        side6[2][i] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    for i in range(len(side5)):
        side5[i][2] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    side2 = rotateStillFace(side2)
    
    return side1, side3, side6, side5, side2

# Rotates the 'back' face of the cube clockwise 90 degrees.
def rotateBack(side1, side5, side6, side3, side4):
    colourSequence = ""
    
    for i in range(len(side1)-1, -1, -1):
        colourSequence = colourSequence + side1[2][i]
        
    for i in range(len(side5)-1, -1, -1):
        colourSequence = colourSequence + side5[i][0]
    
    for i in range(len(side6)):
        colourSequence = colourSequence + side6[0][i]
    
    for i in range(len(side3)):
        colourSequence = colourSequence + side3[i][2]
    
    colourSequence = shiftColourSequence(len(side1), colourSequence, False)
    
    for i in range(len(side1)-1, -1, -1):
        side1[2][i] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    for i in range(len(side5)-1, -1, -1):
        side5[i][0] = colourSequence[0]
        colourSequence = colourSequence[1:]
        
    for i in range(len(side6)):
        side6[0][i] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    for i in range(len(side3)):
        side3[i][2] = colourSequence[0]
        colourSequence = colourSequence[1:]
    
    side4 = rotateStillFace(side4)
    
    return side1, side5, side6, side3, side4

# Contains functions for the Rubik's cube object.
class rubikCube:
    
    # Initialises the sides of the cube
    def __init__(self, cubeSize):
        self.side1 = [["","",""],["","",""],["","",""]] # Green
        self.side2 = [["","",""],["","",""],["","",""]] # White
        self.side3 = [["","",""],["","",""],["","",""]] # Red
        self.side4 = [["","",""],["","",""],["","",""]] # Yellow
        self.side5 = [["","",""],["","",""],["","",""]] # Orange
        self.side6 = [["","",""],["","",""],["","",""]] # Blue
        self.cubeSize = cubeSize
        
        # Fills the cube sides with the correct default colours.
        for i in range(cubeSize):
            for j in range(cubeSize):
                self.side1[i][j] = "G"
                self.side2[i][j] = "W"
                self.side3[i][j] = "R"
                self.side4[i][j] = "Y"
                self.side5[i][j] = "O"
                self.side6[i][j] = "B"
    
    # Displays the current state of the cube to the console. Very useful for
    # debugging!
    def displayState(self):
        
        print("Side 1")
        for i in range(self.cubeSize):
            print(self.side1[i])
            
        print("Side 2")
        for i in range(self.cubeSize):
            print(self.side2[i])
        
        print("Side 3")
        for i in range(self.cubeSize):
            print(self.side3[i])
            
        print("Side 4")
        for i in range(self.cubeSize):
            print(self.side4[i])
        
        print("Side 5")
        for i in range(self.cubeSize):
            print(self.side5[i])
        
        print("Side 6")
        for i in range(self.cubeSize):
            print(self.side6[i])
    
    # Uses the functions from the rotations library to rotate the game cube
    # given the face to be rotated and the number of turns to rotate it by.
    def rotateSide(self, face, turns):
        # Given 'L' as input, rotates the left face by a given number of turns.
        if face == "L":
            for i in range(turns):
                self.side1, self.side2, self.side6, self.side4, self.side5 = rotateLeft(self.side1, self.side2, self.side6, self.side4, self.side5)
        
        # Given 'R' as input, rotates the right face by a given number of turns.
        elif face == "R":
            for i in range(turns):
                self.side1, self.side2, self.side6, self.side4, self.side3 = rotateRight(self.side1, self.side2, self.side6, self.side4, self.side3)
        
        # Given 'U' as input, rotates the up face by a given number of turns.
        elif face == "U":
            for i in range(turns):
                self.side2, self.side3, self.side4, self.side5, self.side6 = rotateUp(self.side2, self.side3, self.side4, self.side5, self.side6)

        # Given 'D' as input, rotates the down face by a given number of turns.
        elif face == "D":
            for i in range(turns):
                self.side2, self.side3, self.side4, self.side5, self.side1 = rotateDown(self.side2, self.side3, self.side4, self.side5, self.side1)
        
        # Given 'F' as input, rotates the front face by a given number of turns.
        elif face == "F":
            for i in range(turns):
                self.side1, self.side3, self.side6, self.side5, self.side2 = rotateFront(self.side1, self.side3, self.side6, self.side5, self.side2)
        
        # Given 'B' as input, rotates the back face by a given number of turns.
        elif face == "B":
            for i in range(turns):
                self.side1, self.side5, self.side6, self.side3, self.side4 = rotateBack(self.side1, self.side5, self.side6, self.side3, self.side4)
    
    # Takes a sequence of moves of unlimited length, decodes the instructions,
    # and follows them sequentially. 'inputSequence' must be a string with
    # pairs consisting of a letter and a number - denoting the face to rotate,
    # and the number of turns to rotate that face.
    def followSequence(self, inputSequence):
        
#        print(inputSequence) # DEBUGGING TOOL ONLY - remove or it spams the console HARD! You have been warned.
        
        for i in range(int(len(inputSequence)/2)):
            if inputSequence[0] == "L":
                self.rotateSide("L", int(inputSequence[1]))
            elif inputSequence[0] == "R":
                self.rotateSide("R", int(inputSequence[1]))
            elif inputSequence[0] == "U":
                self.rotateSide("U", int(inputSequence[1]))
            elif inputSequence[0] == "D":
                self.rotateSide("D", int(inputSequence[1]))
            elif inputSequence[0] == "F":
                self.rotateSide("F", int(inputSequence[1]))
            elif inputSequence[0] == "B":
                self.rotateSide("B", int(inputSequence[1]))
            
            # Removes the last instruction from the sequence once complete.
            inputSequence = inputSequence[2:]
    
    # Randomly shuffles the cube a given number of times to ensure a completely 
    # random shuffle. 25 is recommended as the minimum to ensure a decent 
    # shuffle, but anything more than 100 or so is probably overkill - however 
    # there is no true upper limit given decent hardware.
    def randomShuffle(self, numberOfShuffles):
        
        # Blank string which will later hold the instructions for randomly
        # shuffling the cube.
        shufflingSequence = ""
        
        for i in range(numberOfShuffles):
            # Gets a random integer.
            turnDirection = randint(1,6)
            
            # Uses the random integer to pick a direction to rotate the cube,
            # then adds that instruction to the sequence.
            if turnDirection == 1:
                shufflingSequence = shufflingSequence + "L1" # Left 1 turn
            elif turnDirection == 2:
                shufflingSequence = shufflingSequence + "R1" # Right 1 turn
            elif turnDirection == 3:
                shufflingSequence = shufflingSequence + "U1" # Up 1 turn
            elif turnDirection == 4:
                shufflingSequence = shufflingSequence + "D1" # Down 1 turn
            elif turnDirection == 5:
                shufflingSequence = shufflingSequence + "F1" # Front 1 turn
            elif turnDirection == 6:
                shufflingSequence = shufflingSequence + "B1" # Back 1 turn
        
        # Uses the followSequence function to follow the randomly generated
        # sequence.
        self.followSequence(shufflingSequence)

# Initialises the game cube from the rubikCube class with a cube size of 3.
a = rubikCube(3) 

# Checks whether the 'green cross' step has been completed correctly. Takes one
# side matrix as input.
def checkGreenCross(side):
    # Returns false if any of the green cross pieces are out of position.
    if side[0][1] != "G":
        return False
    elif side[1][0] != "G":
        return False
    elif side[1][2] != "G":
        return False
    elif side[2][1] != "G":
        return False
    elif side[1][1] != "G":
        return False
    
    # Returns true otherwise.
    else:
        return True
    
# Checks whether the 'green side' step has been completed correctly. Takes one
# side matrix as input.
def checkGreenSide(side):
    
    # Cycles through every entry in the matrix and returns false if any are not
    # green.
    for i in range(len(side)):
        for j in range(len(side)):
            if side[i][j] != "G":
                return False
            
    # Returns true otherwise.
    return True

# Checks whether the edge pieces adjacent the green side match the centre 
# colour for their side. Takes 4 side matrices as inputs - these should be the
# matrices of the sides adjacent to the green side.
def checkAlignedCenters(side2, side3, side4, side5):
    
    # Returns false if the adjacent white edge is not in the correct position.
    if side2[2][1] != "W":
        return False
    # Returns false if the adjacent red edge is not in the correct position.
    elif side3[2][1] != "R":
        return False
    # Returns false if the adjacent yellow edge is not in the correct position.
    elif side4[2][1] != "Y":
        return False
    # Returns false if the adjacent orange edge is not in the correct position.
    elif side5[2][1] != "O":
        return False
    
    # Returns true otherwise.
    else:
        return True

# Checks whether the corner pieces adjacent the green side match the centre
# colour for their side. Takes 4 side matrices as inputs - these should be
# the matrices of the sides adjacent to the green side.
def checkAlignedCorners(side2, side3, side4, side5):
    
    # Returns false if the green/white/orange corner is incorrectly placed.
    if side2[2][0] != "W" or side5[2][2] != "O":
        return False
    # Returns false if the green/red/white corner is incorrectly placed.
    elif side3[2][0] != "R" or side2[2][2] != "W":
        return False
    # Returns false if the green/yellow/red corner is incorrectly placed.
    elif side4[2][0] != "Y" or side3[2][2] != "R":
        return False
    # Returns false if the green/orange/yellow corner is incorrectly placed.
    elif side5[2][0] != "O" or side4[2][2] != "Y":
        return False
    
    # Returns true otherwise.
    else:
        return True

# Checks whether the two rows closest the green side on the white, red, yellow
# and orange sides are solved correctly. Takes 4 side matrices as input - these
# should be the matrices of the sides adjacent to the green side.
def checkFirstTwoRows(side2, side3, side4, side5):
    
    for i in range(len(side2)-1):
        for j in range(len(side2)):
            if side2[i+1][j] != "W":
                return False
    
    for i in range(len(side3)-1):
        for j in range(len(side3)):
            if side3[i+1][j] != "R":
                return False
    
    for i in range(len(side4)-1):
        for j in range(len(side4)):
            if side4[i+1][j] != "Y":
                return False
    
    for i in range(len(side5)-1):
        for j in range(len(side5)):
            if side5[i+1][j] != "O":
                return False

# Checks whether the 'blue cross' step has been completed correctly. Takes one
# side matrix as input.
def checkBlueCross(side):
    # Returns false if any of the blue cross pieces are out of position.
    if side[0][1] != "B":
        return False
    elif side[1][0] != "B":
        return False
    elif side[1][2] != "B":
        return False
    elif side[2][1] != "B":
        return False
    elif side[1][1] != "B":
        return False
    
    # Returns true otherwise.
    else:
        return True
    
# Checks whether the 'blue side' step has been completed correctly. Takes one
# side matrix as input.
def checkBlueSide(side):
    
    # Cycles through every entry in the matrix and returns false if any are not
    # blue.
    for i in range(len(side)):
        for j in range(len(side)):
            if side[i][j] != "B":
                return False
            
    # Returns true otherwise.
    return True

# Checks whether the top layer corners are in the correct positions. 
# Takes 4 side matrices as input - these should be the matrices of the sides 
# adjacent to the green side.
def checkTopLayerCorners(side2, side3, side4, side5):
    # Returns false if any of the top layer corners are out of position.
    if side2[0][0] != "W" or side5[0][2] != "O":
        return False
    elif side3[0][0] != "R" or side2[0][2] != "W":
        return False
    elif side4[0][0] != "Y" or side3[0][2] != "R":
        return False
    elif side5[0][0] != "O" or side4[0][2] != "Y":
        return False
    
    # Returns true otherwise.
    else:
        return True
    
def checkCube(side1, side2, side3, side4, side5, side6):
    # Cycles through every entry in side 1 and returns false if any are not
    # green.
    for i in range(len(side1)):
        for j in range(len(side1)):
            if side1[i][j] != "G":
                return False
            
    # Cycles through every entry in side 2 and returns false if any are not
    # white.
    for i in range(len(side2)):
        for j in range(len(side2)):
            if side2[i][j] != "W":
                return False
            
    # Cycles through every entry in side 3 and returns false if any are not
    # red.
    for i in range(len(side3)):
        for j in range(len(side3)):
            if side3[i][j] != "R":
                return False
    
    # Cycles through every entry in side 4 and returns false if any are not
    # yellow.
    for i in range(len(side4)):
        for j in range(len(side4)):
            if side4[i][j] != "Y":
                return False
    
    # Cycles through every entry in side 5 and returns false if any are not
    # orange.
    for i in range(len(side5)):
        for j in range(len(side5)):
            if side5[i][j] != "O":
                return False
    
    # Cycles through every entry in side 6 and returns false if any are not
    # blue.
    for i in range(len(side6)):
        for j in range(len(side6)):
            if side6[i][j] != "B":
                return False
    
    # Returns true otherwise.
    return True
    
def solveGreenCross():
    sequenceToFollow = ""
    counter = 0
    while checkGreenCross(a.side1) != True:
        a.followSequence(sequenceToFollow)
        sequenceToFollow = ""    
        if a.side1[1][0] != "G":
            if a.side2[1][0] == "G":
                sequenceToFollow = "L1"
                continue
            elif a.side6[1][0] == "G":
                sequenceToFollow = "L2"
                continue
            elif a.side4[1][2] == "G":
                sequenceToFollow = "L3"
                continue
            
        if a.side1[0][1] != "G":
            if a.side3[1][0] == "G":
                sequenceToFollow = "F1"
                continue
            elif a.side6[2][1] == "G":
                sequenceToFollow = "F2"
                continue
            elif a.side5[1][2] == "G":
                sequenceToFollow = "F3"
                continue
        
        if a.side1[1][2] != "G":
            if a.side4[1][0] == "G":
                sequenceToFollow = "R1"
                continue
            elif a.side6[1][2] == "G":
                sequenceToFollow = "R2"
                continue
            elif a.side2[1][2] == "G":
                sequenceToFollow = "R3"
                continue
        
        if a.side1[2][1] != "G":
            if a.side5[1][0] == "G":
                sequenceToFollow = "B1"
                continue
            elif a.side6[0][1] == "G":
                sequenceToFollow = "B2"
                continue
            elif a.side3[1][2] == "G":
                sequenceToFollow = "B3"
                continue
        
        if a.side5[2][1] == "G":
            sequenceToFollow = "D1B1D3L3"
            continue
        elif a.side5[0][1] == "G":
            if a.side1[1][0] == "G":
                sequenceToFollow = "D1"
                continue
            else:
                sequenceToFollow = "L2D1B1D3L3"
                continue
        
        if a.side4[2][1] == "G":
            if a.side1[2][1] != "G":
                sequenceToFollow = "B1D3R1"
                continue
            else:
                sequenceToFollow = "D1"
                continue
        elif a.side4[0][1] == "G":
            if a.side1[1][0] == "G":
                sequenceToFollow = "D1"
                continue
            else:
                sequenceToFollow = "U2L2D1B1D3L3"
                continue
        
        if a.side3[2][1] == "G":
            sequenceToFollow = "D2B1D3L3"
            continue
        elif a.side3[0][1] == "G":
            if a.side1[1][0] == "G":    
                sequenceToFollow = "D1"
                continue
            else:
                sequenceToFollow = "U3L2D1B1D3L3"
                continue
        
        if a.side2[0][1] == "G":
            if a.side1[1][0] == "G":
                sequenceToFollow = "D1"
                continue
            else:
                sequenceToFollow = "F3L3U3L1F2"
                continue
        
        sequenceToFollow = "D1"
        
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break

def solveGreenCorners():
    sequenceToFollow = ""
    counter = 0
    errorCounter = 0
    
    while checkGreenSide(a.side1) != True:
        a.followSequence(sequenceToFollow)
        sequenceToFollow = ""
        
        if a.side1[0][0] != "G":
            if a.side2[0][0] == "G":
                sequenceToFollow = "F1U1F3"
                continue
            elif a.side3[0][0] == "G":
                sequenceToFollow = "U1F1U1F3"
                continue
            elif a.side4[0][0] == "G":
                sequenceToFollow = "U2F1U1F3"
                continue
            elif a.side5[0][0] == "G":
                sequenceToFollow = "U3F1U1F3"
                continue
            
            elif a.side6[2][0] == "G":
                sequenceToFollow = "L3U2L1U1L3U3L1"
                continue
            elif a.side6[2][2] == "G":
                sequenceToFollow = "U1L3U2L1U1L3U3L1"
                continue
            elif a.side6[0][2] == "G":
                sequenceToFollow = "U2L3U2L1U1L3U3L1"
                continue
            elif a.side6[0][0] == "G":
                sequenceToFollow = "U3L3U2L1U1L3U3L1"
                continue
            
            elif a.side4[0][2] == "G":
                sequenceToFollow = "U2L3U3L1U2L3U3L1"
                continue
            elif a.side2[2][0] == "G":
                sequenceToFollow = "L3U1L1"
                continue
            
            elif a.side5[2][2] == "G":
                sequenceToFollow = "F1U1F3"
                continue
        
        # This code is super bugged - for some reason it works, but it hangs
        # the program sometimes unless the errorCounter and break is in there.
        # Some super specific pattern in the cube causes it to hang - it only
        # occurs about once in 100,000 simulations! Either way, don't touch
        # this else statement unless you're willing to actually spend the many 
        # hours it will take to properly fix this bug. You have been warned!
        else:
            sequenceToFollow = "D1"
            errorCounter += 1
            if errorCounter > 10: # Failsafe until the bug is fixed.
                break
            continue
            
        sequenceToFollow = "U1"
        
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break
        
def fixAlignedCenters():
    sequenceToFollow = ""
    counter = 0
    
    while checkAlignedCenters(a.side2, a.side3, a.side4, a.side5) != True:
        a.followSequence(sequenceToFollow)
        sequenceToFollow = ""
        
        # If the layer is correct but just needs rotating.
        if a.side2[2][1] == "R" and a.side3[2][1] == "Y" and a.side4[2][1] == "O" and a.side5[2][1] == "W":
            sequenceToFollow = "D1"
            continue
        elif a.side2[2][1] == "Y" and a.side3[2][1] == "O" and a.side4[2][1] == "W" and a.side5[2][1] == "R":
            sequenceToFollow = "D2"
            continue
        elif a.side2[2][1] == "O" and a.side3[2][1] == "W" and a.side4[2][1] == "R" and a.side5[2][1] == "Y":
            sequenceToFollow = "D3"
            continue
        
        # If there are two colours which need swapping.
        if a.side5[2][1] == "Y" and a.side4[2][1] == "O":
            sequenceToFollow = "F3B1L1F1B3U3R1L3B1R3L1U1F3B1L1F1B3"
            continue
        elif a.side5[2][1] == "R" and a.side3[2][1] == "O":
            sequenceToFollow = "F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif a.side5[2][1] == "W" and a.side2[2][1] == "O":
            sequenceToFollow = "R3L1F1L3R1U3F3B1L1F1B3U1R3L1F1L3R1"
            continue
        elif a.side2[2][1] == "Y" and a.side4[2][1] == "W":
            sequenceToFollow = "L1R3F1L2R2B1L2R2F1L3R1"
            continue
        elif a.side2[2][1] == "R" and a.side3[2][1] == "W":
            sequenceToFollow = "L1R3D1U3R3D3U1F2L3R1"
            continue
        elif a.side4[2][1] == "R" and a.side3[2][1] == "Y":
            sequenceToFollow = "B3F1D1U3B3U1D3R2F3B1"
            continue
        
        # If there are three colours which need rotationally swapping.
        if a.side2[2][1] == "R" and a.side3[2][1] == "Y" and a.side4[2][1] == "W":
            sequenceToFollow = "L1R3F1L2R2B1L2R2F1L3R1B3F1D1U3B3U1D3R2F3B1"
            continue
        elif a.side2[2][1] == "Y" and a.side3[2][1] == "W" and a.side4[2][1] == "R":
            sequenceToFollow = "L1R3D1U3R3D3U1F2L3R1B3F1D1U3B3U1D3R2F3B1"
            continue
        elif a.side2[2][1] == "O" and a.side3[2][1] == "W" and a.side5[2][1] == "R":
            sequenceToFollow = "L1R3D1U3R3D3U1F2L3R1F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif a.side2[2][1] == "R" and a.side3[2][1] == "O" and a.side5[2][1] == "W":
            sequenceToFollow = "R3L1F1L3R1U3F3B1L1F1B3U1R3L1F1L3R1F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif a.side2[2][1] == "O" and a.side4[2][1] == "W" and a.side5[2][1] == "Y":
            sequenceToFollow = "L1R3F1L2R2B1L2R2F1L3R1F3B1L1F1B3U3R1L3B1R3L1U1F3B1L1F1B3"
            continue
        elif a.side3[2][1] == "Y" and a.side4[2][1] == "O" and a.side5[2][1] == "R":
            sequenceToFollow = "F3B1L1F2B2R1F2B2L1F1B3F3B1L1F1B3U3R1L3B1R3L1U1F3B1L1F1B3"
            continue
        elif a.side3[2][1] == "O" and a.side4[2][1] == "R" and a.side5[2][1] == "Y":
            sequenceToFollow = "F3B1L1F2B2R1F2B2L1F1B3B3F1D1U3B3U1D3R2F3B1"
        
        # Other random cases - usually specifically dealing with combinations
        # of smaller swaps.
        if a.side2[2][1] == "R" and a.side3[2][1] == "O" and a.side4[2][1] == "W" and a.side5[2][1] == "Y":
            sequenceToFollow = "L1R3F1L2R2B1L2R2F1L3R1F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif a.side2[2][1] == "O" and a.side3[2][1] == "W" and a.side4[2][1] == "Y" and a.side5[2][1] == "R":
            sequenceToFollow = "D1L1R3F1L2R2B1L2R2F1L3R1F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif a.side2[2][1] == "W" and a.side3[2][1] == "Y" and a.side4[2][1] == "R" and a.side5[2][1] == "O":
            sequenceToFollow = "D2L1R3F1L2R2B1L2R2F1L3R1F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif a.side2[2][1] == "Y" and a.side3[2][1] == "R" and a.side4[2][1] == "O" and a.side5[2][1] == "W":
            sequenceToFollow = "D3L1R3F1L2R2B1L2R2F1L3R1F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif a.side2[2][1] == "Y" and a.side3[2][1] == "W" and a.side4[2][1] == "O" and a.side5[2][1] == "R":
            sequenceToFollow = "L1R3F1L2R2B1L2R2F1L3R1L1R3D1U3R3D3U1F2L3R1F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif a.side2[2][1] == "Y" and a.side3[2][1] == "O" and a.side4[2][1] == "R" and a.side5[2][1] == "W":
            sequenceToFollow = "D1F3B1L1F2B2R1F2B2L1F1B3F3B1L1F1B3U3R1L3B1R3L1U1F3B1L1F1B3"
            continue
        elif a.side2[2][1] == "O" and a.side3[2][1] == "Y" and a.side4[2][1] == "W" and a.side5[2][1] == "R":
            sequenceToFollow = "D2F3B1L1F1B3U3R1L3B1R3L1U1F3B1L1F1B3"
            continue
        
        sequenceToFollow == "D1"
        
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break

def fixAlignedCorners():
    sequenceToFollow = ""
    counter = 0
    
    while checkAlignedCorners(a.side2, a.side3, a.side4, a.side5) != True:
        a.followSequence(sequenceToFollow)
        sequenceToFollow = ""
        
        if a.side2[2][0] != "W" or a.side5[2][2] != "O":
            if a.side2[2][2] == "O" and a.side3[2][0] == "W":
                sequenceToFollow = "R1U2R3F1U3F3U2F3U1F1"
                continue
            elif a.side3[2][2] == "O" and a.side4[2][0] == "W":
                sequenceToFollow = "B1U1B3U2F1U3F3U1R3U1R1"
                continue
            elif a.side4[2][2] == "O" and a.side5[2][0] == "W":
                sequenceToFollow = "B3U1B1F1U3F3B3U1B1"
                continue
        
        if a.side3[2][0] != "R" or a.side2[2][2] != "W":
            if a.side3[2][2] == "W" and a.side4[2][0] == "R":
                sequenceToFollow = "B1U2B3R1U3R3U1R3U2R1"
                continue
            elif a.side4[2][2] == "W" and a.side5[2][0] == "R":
                sequenceToFollow = "L1U1L3U2R1U3R3B3U2B1"
                continue
            
        if a.side4[2][0] != "Y" or a.side3[2][2] != "R":
            if a.side4[2][2] == "R" and a.side5[2][0] == "Y":
                sequenceToFollow = "L1U2L3B1U3B3U2B3U1B1"
                continue
            
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break


def solveFirstTwoRows():
    sequenceToFollow = ""
    counter = 0
    
    while checkFirstTwoRows(a.side2, a.side3, a.side4, a.side5) != True:
        a.followSequence(sequenceToFollow)
        sequenceToFollow = ""
        
        # If the orange and white edge piece is not correctly placed
        if a.side2[1][0] != "W" or a.side5[1][2] != "O":
            # If the orange and white edge piece is in the top layer
            if a.side6[2][1] == "O" and a.side2[0][1] == "W":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            elif a.side6[1][2] == "O" and a.side3[0][1] == "W":
                sequenceToFollow = "L3U1L1U1F1U3F3"
                continue
            elif a.side6[0][1] == "O" and a.side4[0][1] == "W":
                sequenceToFollow = "U1L3U1L1U1F1U3F3"
                continue
            elif a.side6[1][0] == "O" and a.side5[0][1] == "W":
                sequenceToFollow = "U2L3U1L1U1F1U3F3"
                continue
            
            # If the orange and white edge piece is inverted in the top layer.
            elif a.side6[2][1] == "W" and a.side2[0][1] == "O":
                sequenceToFollow = "U2F1U3F3U3L3U1L1" ######
                continue
            elif a.side6[1][2] == "W" and a.side3[0][1] == "O":
                sequenceToFollow = "U3F1U3F3U3L3U1L1"
                continue
            elif a.side6[0][1] == "W" and a.side4[0][1] == "O":
                sequenceToFollow = "F1U3F3U3L3U1L1"
                continue
            elif a.side6[1][0] == "W" and a.side5[0][1] == "O":
                sequenceToFollow = "U1F1U3F3U3L3U1L1"
                continue
            
            # If the orange and white edge piece is inverted in the correct position.
            elif a.side2[1][0] == "O" and a.side5[1][2] == "W":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            
            # If the orange and white edge piece is elsewhere in the middle layer.
            elif a.side3[1][0] == "W" and a.side2[1][2] == "O":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            elif a.side4[1][0] == "W" and a.side3[1][2] == "O":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            elif a.side5[1][0] == "W" and a.side4[1][2] == "O":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
            
            # If the orange and white edge piece is inverted elsewhere in the middle layer.
            elif a.side3[1][0] == "O" and a.side2[1][2] == "W":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            elif a.side4[1][0] == "O" and a.side3[1][2] == "W":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            elif a.side5[1][0] == "O" and a.side4[1][2] == "W":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
        
        # If the white and red edge piece is not correctly placed
        elif a.side3[1][0] != "R" or a.side2[1][2] != "W":
            # If the white and red edge piece is in the top layer
            if a.side6[1][2] == "W" and a.side3[0][1] == "R":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            elif a.side6[0][1] == "W" and a.side4[0][1] == "R":
                sequenceToFollow = "F3U1F1U1R1U3R3"
                continue
            elif a.side6[1][0] == "W" and a.side5[0][1] == "R":
                sequenceToFollow = "U1F3U1F1U1R1U3R3"
                continue
            elif a.side6[2][1] == "W" and a.side2[0][1] == "R":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            
            # If the white and red edge piece is inverted in the top layer
            elif a.side6[1][2] == "R" and a.side3[0][1] == "W":
                sequenceToFollow = "U2R1U3R3U3F3U1F1"
                continue
            elif a.side6[0][1] == "R" and a.side4[0][1] == "W":
                sequenceToFollow = "U3R1U3R3U3F3U1F1"
                continue
            elif a.side6[1][0] == "R" and a.side5[0][1] == "W":
                sequenceToFollow = "R1U3R3U3F3U1F1"
                continue
            elif a.side6[2][1] == "R" and a.side2[0][1] == "W":
                sequenceToFollow = "U1R1U3R3U3F3U1F1"
                continue
            
            # If the white and red edge piece is inverted in the correct position.
            elif a.side3[1][0] == "W" and a.side2[1][2] == "R":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            
            # If the white and red edge piece is elsewhere in the middle layer
            elif a.side4[1][0] == "R" and a.side3[1][2] == "W":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            elif a.side5[1][0] == "R" and a.side4[1][2] == "W":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
            elif a.side2[1][0] == "R" and a.side5[1][2] == "W":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            
            # If the white and red edge piece is inverted elsewhere in the middle layer
            elif a.side4[1][0] == "W" and a.side3[1][2] == "R":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            elif a.side5[1][0] == "W" and a.side4[1][2] == "R":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
            elif a.side2[1][0] == "W" and a.side5[1][2] == "R":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            
        # If the red and yellow edge piece is not correctly placed.
        elif a.side4[1][0] != "Y" or a.side3[1][2] != "R":
            # If the red and yellow edge piece is in the top layer
            if a.side6[0][1] == "R" and a.side4[0][1] == "Y":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            elif a.side6[1][0] == "R" and a.side5[0][1] == "Y":
                sequenceToFollow = "R3U1R1U1B1U3B3"
                continue
            elif a.side6[2][1] == "R" and a.side2[0][1] == "Y":
                sequenceToFollow = "U1R3U1R1U1B1U3B3"
                continue
            elif a.side6[1][2] == "R" and a.side3[0][1] == "Y":
                sequenceToFollow = "U2R3U1R1U1B1U3B3"
                continue
            
            # If the red and yellow edge piece is inverted in the top layer
            elif a.side6[0][1] == "Y" and a.side4[0][1] == "R":
                sequenceToFollow = "U1B1U3B3U3R3U1R1"
                continue
            elif a.side6[1][0] == "Y" and a.side5[0][1] == "R":
                sequenceToFollow = "U2B1U3B3U3R3U1R1"
                continue
            elif a.side6[2][1] == "Y" and a.side2[0][1] == "R":
                sequenceToFollow = "U3B1U3B3U3R3U1R1"
                continue
            elif a.side6[1][2] == "Y" and a.side3[0][1] == "R":
                sequenceToFollow = "B1U3B3U3R3U1R1"
                continue
            
            # If the red and yellow edge piece is inverted in the correct position
            elif a.side4[1][0] == "R" and a.side3[1][2] == "Y":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            
            # If the red and yellow edge piece is elsewhere in the middle layer
            elif a.side5[1][0] == "Y" and a.side4[1][2] == "R":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
            elif a.side2[1][0] == "Y" and a.side5[1][2] == "R":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            elif a.side3[1][0] == "Y" and a.side2[1][2] == "R":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            
            # If the red and yellow edge piece is inverted elsewhere in the middle layer
            elif a.side5[1][0] == "R" and a.side4[1][2] == "Y":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
            elif a.side2[1][0] == "R" and a.side5[1][2] == "Y":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            elif a.side3[1][0] == "R" and a.side2[1][2] == "Y":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
        
        # If the yellow and orange edge piece is not correctly placed.
        elif a.side5[1][0] != "O" or a.side4[1][2] != "Y":
            # If the yellow and orange edge piece is in the top layer
            if a.side6[1][0] == "Y" and a.side5[0][1] == "O":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
            elif a.side6[2][1] == "Y" and a.side2[0][1] == "O":
                sequenceToFollow = "B3U1B1U1L1U3L3"
                continue
            elif a.side6[1][2] == "Y" and a.side3[0][1] == "O":
                sequenceToFollow = "U1B3U1B1U1L1U3L3"
                continue
            elif a.side6[0][1] == "Y" and a.side4[0][1] == "O":
                sequenceToFollow = "U2B3U1B1U1L1U3L3"
                continue
            
            # If the yellow and orange edge piece is inverted in the top layer
            elif a.side6[1][0] == "O" and a.side5[0][1] == "Y":
                sequenceToFollow = "U2L1U3L3U3B3U1B1"
                continue
            elif a.side6[2][1] == "O" and a.side2[0][1] == "Y":
                sequenceToFollow = "U3L1U3L3U3B3U1B1"
                continue
            elif a.side6[1][2] == "O" and a.side3[0][1] == "Y":
                sequenceToFollow = "L1U3L3U3B3U1B1"
                continue
            elif a.side6[0][1] == "O" and a.side4[0][1] == "Y":
                sequenceToFollow = "U1L1U3L3U3B3U1B1"
                continue
            
            # If the yellow and orange edge piece is inverted in the correct position.
            elif a.side5[1][0] == "Y" and a.side4[1][2] == "O":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
            
            # If the yellow and orange edge piece is elsewhere in the middle layer
            elif a.side2[1][0] == "O" and a.side5[1][2] == "Y":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            elif a.side3[1][0] == "O" and a.side2[1][2] == "Y":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            elif a.side4[1][0] == "O" and a.side3[1][2] == "Y":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            
            # If the yellow and orange edge piece is elsewhere in the middle layer
            elif a.side2[1][0] == "Y" and a.side5[1][2] == "O":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            elif a.side3[1][0] == "Y" and a.side2[1][2] == "O":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            elif a.side4[1][0] == "Y" and a.side3[1][2] == "O":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break

# Function for solving the 'blue cross' step of the cube. Should only be run
# as part of the totalSolve() function, as it will not work unless all previous
# solution steps have been completed.
def solveBlueCross():
    # Sets up variables for function to operate correctly.
    counter = 0
    sequenceToFollow = ""
    
    # Runs until the blue cross is formed.
    while checkBlueCross != True:
        # Follows the sequence from the last run of the loop, then clears the
        # sequence string ready for the next instruction.
        a.followSequence(sequenceToFollow)
        sequenceToFollow = ""
        
        # Gets the number of correctly positioned blue pieces. Used to decide
        # what state the cube is already in.
        numberOfCorrectBlue = 0
        if a.side6[0][1] == "B":
            numberOfCorrectBlue += 1
        if a.side6[1][0] == "B":
            numberOfCorrectBlue += 1
        if a.side6[1][2] == "B":
            numberOfCorrectBlue += 1
        if a.side6[2][1] == "B":
            numberOfCorrectBlue += 1
    
        # If no blue edge pieces are in the correct place
        if numberOfCorrectBlue == 0:
            sequenceToFollow = "F1U1R1U3R3F3"
            continue
        
        # If two of the blue edge pieces are in the correct place
        elif numberOfCorrectBlue == 2:
            # If the two blue edge pieces form a 'V' shape
            if a.side6[0][1] == "B" and a.side6[1][0] == "B":
                sequenceToFollow = "F1U1R1U3R3F3"
                continue
            elif a.side6[1][0] == "B" and a.side6[2][1] == "B":
                sequenceToFollow = "U1F1U1R1U3R3F3"
                continue
            elif a.side6[2][1] == "B" and a.side6[1][2] == "B":
                sequenceToFollow = "U2F1U1R1U3R3F3"
                continue
            elif a.side6[1][2] == "B" and a.side6[0][1] == "B":
                sequenceToFollow = "U3F1U1R1U3R3F3"
                continue
            
            # If the two blue edge pieces form a horizontal line
            elif a.side6[1][0] == "B" and a.side6[1][2] == "B":
                sequenceToFollow = "F1R1U1R3U3F3"
                continue
            elif a.side6[0][1] == "B" and a.side6[2][1] == "B":
                sequenceToFollow = "U1F1R1U1R3U3F3"
                continue
        
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break

def solveBlueSide():
    counter = 0
    sequenceToFollow = ""
    
    while checkBlueSide(a.side6) != True:
        a.followSequence(sequenceToFollow)
        sequenceToFollow = ""
        
        numberOfCorrectBlue = 0
        if a.side6[0][0] == "B":
            numberOfCorrectBlue += 1
        if a.side6[0][2] == "B":
            numberOfCorrectBlue += 1
        if a.side6[2][0] == "B":
            numberOfCorrectBlue += 1
        if a.side6[2][2] == "B":
            numberOfCorrectBlue += 1
        
        if numberOfCorrectBlue == 0:
            if a.side5[0][2] != "B":
                sequenceToFollow = "U1"
                continue
            else:
                sequenceToFollow = "R1U1R3U1R1U2R3"
                continue
            
        if numberOfCorrectBlue == 1:
            if a.side6[2][0] != "B":
                sequenceToFollow = "U1"
                continue
            else:
                sequenceToFollow = "R1U1R3U1R1U2R3"
                continue
                
        elif numberOfCorrectBlue == 2:
            if a.side2[0][0] != "B":
                sequenceToFollow = "U1"
                continue
            else:
                sequenceToFollow = "R1U1R3U1R1U2R3"
                continue
        
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break

# Function for solving the top layer corners of the cube. Should only be run
# as part of the totalSolve() function, as it will not work unless all previous
# solution steps have been completed.
def solveTopLayerCorners():
    # Sets up variables for function to operate correctly.
    counter = 0
    sequenceToFollow = ""
    
    # Runs until the top layer corners are in the correct position.
    while checkTopLayerCorners(a.side2, a.side3, a.side4, a.side5) != True:
        a.followSequence(sequenceToFollow)
        sequenceToFollow = ""
        
        # Gets the number of correctly positioned corner pieces. Used to decide
        # what state the cube is already in.
        numberOfCorrectCorners = 0
        if a.side2[0][0] == "W" and a.side5[0][2] == "O":
            numberOfCorrectCorners += 1
        if a.side3[0][0] == "R" and a.side2[0][2] == "W":
            numberOfCorrectCorners += 1
        if a.side4[0][0] == "Y" and a.side3[0][2] == "R":
            numberOfCorrectCorners += 1
        if a.side5[0][0] == "O" and a.side4[0][2] == "Y":
            numberOfCorrectCorners += 1
            
        # Rotates the up face until two corners are in the correct position.
        # If all previous steps completed correctly, there should always be
        # two correct corner pieces to rotate into position.
        if numberOfCorrectCorners != 2:
            sequenceToFollow = "U1"
        
        # When the two correct pieces are in position, selects the correct
        # algorithm to follow and runs it.
        else:
            # When the two correct pieces are diagonally opposite each other.
            if (a.side2[0][0] == "W" and a.side5[0][2] == "O") and (a.side4[0][0] == "Y" and a.side3[0][2] == "R"):
                sequenceToFollow = "R3F1R3B2R1F3R3B2R2U3"
                continue
            elif (a.side3[0][0] == "R" and a.side2[0][2] == "W") and (a.side5[0][0] == "O" and a.side4[0][2] == "Y"):
                sequenceToFollow = "R3F1R3B2R1F3R3B2R2U3"
                continue
            
            # When the two correct pieces include the same face of the cube.
            elif (a.side4[0][0] == "Y" and a.side3[0][2] == "R") and (a.side5[0][0] == "O" and a.side4[0][2] == "Y"):
                sequenceToFollow = "R3F1R3B2R1F3R3B2R2U3"
                continue
            elif (a.side2[0][0] == "W" and a.side5[0][2] == "O") and (a.side5[0][0] == "O" and a.side4[0][2] == "Y"):
                sequenceToFollow = "B3R1B3L2B1R3B3L2B2U3"
                continue
            elif (a.side3[0][0] == "R" and a.side2[0][2] == "W") and (a.side2[0][0] == "W" and a.side5[0][2] == "O"):
                sequenceToFollow = "L3B1L3F2L1B3L3F2L2U3"
                continue
            elif (a.side4[0][0] == "Y" and a.side3[0][2] == "R") and (a.side3[0][0] == "R" and a.side2[0][2] == "W"):
                sequenceToFollow = "F3L1F3R2F1L3F3R2F2U3"
                continue
            
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break
        
# Function for solving the top layer edges of the cube. Should only be run as
# part of the totalSolve() function, as it will not work unless all previous
# solution steps have been completed.
def solveTopLayerEdges():
    # Sets up variables for function to operate correctly.
    counter = 0
    sequenceToFollow = ""

    # Runs until the cube is solved.
    while checkCube(a.side1, a.side2, a.side3, a.side4, a.side5, a.side6) != True:
        a.followSequence(sequenceToFollow)
        sequenceToFollow = ""
    
        # Gets the number of correctly positioned edge pieces. Used to decide
        # what state the cube is already in.
        numberOfCorrectEdges = 0
        if a.side2[0][1] == "G":
            numberOfCorrectEdges += 1
        if a.side3[0][1] == "R":
            numberOfCorrectEdges += 1
        if a.side4[0][1] == "Y":
            numberOfCorrectEdges += 1
        if a.side5[0][1] == "O":
            numberOfCorrectEdges += 1
        
        # If no edges are correctly positioned, run the sequence anyway and
        # within 2 iterations of the loop one should be in the correct spot.
        if numberOfCorrectEdges == 0:
            sequenceToFollow = "F2U1L1R3F2L3R1U1F2"
            continue
        
        # Otherwise find and run the correct algorithm.
        elif numberOfCorrectEdges == 1:
            # If the red top edge piece is correct.
            if a.side3[0][1] == "R":
                sequenceToFollow = "L2U1B1F3L2B3F1U1L2"
                continue
            
            # If the yellow top edge piece is correct.
            elif a.side4[0][1] == "Y":
                sequenceToFollow = "F2U1L1R3F2L3R1U1F2"
                continue
            
            # If the orange top edge piece is correct.
            elif a.side5[0][1] == "O":
                sequenceToFollow = "R2U1F1B3R2F3B1U1R2"
                continue
            
            # If the white top edge piece is correct.
            elif a.side6[0][1] == "W":
                sequenceToFollow = "B2U1R1L3B2R3L1U1B2"
                continue
            
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break
        
# Calls each of the solving functions in order, completely solving the cube!
def totalSolve():
    solveGreenCross()
    solveGreenCorners()
    fixAlignedCenters()
    fixAlignedCorners()
    solveFirstTwoRows()
    solveBlueCross()
    solveBlueSide()
    solveTopLayerCorners()
    solveTopLayerEdges()

# Developer function.
# Useful for running many simulations of randomly shuffling the cube, then
# solving it and testing to ensure that the cube is arranged correctly. Prints
# information to the console after running all simulations indicating success
# or failure statistics.
def runSimulations(numberOfSimulations):
    # Used to count the total number of successes and failures.
    successCounter = 0
    failCounter = 0
    
    # Counts the number of failures of a specific type.
    greenCrossFailCounter = 0
    greenSideFailCounter = 0
    alignedCentersFailCounter = 0
    alignedCornersFailCounter = 0
    firstTwoRowsFailCounter = 0
    blueCrossFailCounter = 0
    blueSideFailCounter = 0
    topLayerCornersFailCounter = 0
    cubeFailCounter = 0

    # Used for estimating the time remaining on the simulations.
    lastPercentageComplete = 0
    startTime = time.time()
    
    # Loop runs until the total number of simulations completed is the same as
    # the number of simulations required.
    while (successCounter + failCounter) < numberOfSimulations:
        
        # Randomly shuffles the cube 100 times - enough to guarantee a random
        # shuffle.
        a.randomShuffle(100)
        
        # Runs the solving functions to complete the cube.
        totalSolve()
        
        # Checks if the green cross was completed correctly.
        if checkGreenCross(a.side1) == False:
            failCounter += 1
            greenCrossFailCounter += 1
            
        # Checks if the green side was completed correctly.
        elif checkGreenSide(a.side1) == False:
            failCounter += 1
            greenSideFailCounter += 1
            
        # Checks if the centre edges adjacent the green side are aligned
        # correctly.
        elif checkAlignedCenters(a.side2, a.side3, a.side4, a.side5) == False:
            failCounter += 1
            alignedCentersFailCounter += 1
        
        # Checks if the corner pieces adjacent the green side are aligned
        # correctly.
        elif checkAlignedCorners(a.side2, a.side3, a.side4, a.side5) == False:
            failCounter += 1
            alignedCornersFailCounter += 1
        
        # Checks if the first two rows closest the green side on the white,
        # red, yellow and orange sides have been completed correctly.
        elif checkFirstTwoRows(a.side2, a.side3, a.side4, a.side5) == False:
            failCounter += 1
            firstTwoRowsFailCounter += 1
        
        elif checkBlueCross(a.side6) == False:
            failCounter += 1
            blueCrossFailCounter += 1
            
        elif checkBlueSide(a.side6) == False:
            failCounter += 1
            blueSideFailCounter += 1
            
        elif checkTopLayerCorners(a.side2, a.side3, a.side4, a.side5) == False:
            failCounter += 1
            topLayerCornersFailCounter += 1
            
        elif checkCube(a.side1, a.side2, a.side3, a.side4, a.side5, a.side6) == False:
            failCounter += 1
            cubeFailCounter += 1
        
        # If the simulation passes all checks, adds 1 to the success counter.
        else:
            successCounter += 1
        
        # Calculates the percentage completion of all the simulations.
        percentageComplete = ((successCounter + failCounter)/numberOfSimulations) * 100
        
        # If the percentage completion (as an integer) has increased, prints
        # the percentage completion and the estimated time remaining to the
        # console.
        if int(percentageComplete) > int(lastPercentageComplete):
            print(str(int(percentageComplete)) + "% done on " + str(int(numberOfSimulations)) + " simulations.")
            
            # Time data
            splitTime = time.time() - startTime
            timePerPercent = splitTime / percentageComplete

            estTimeRemaining = int(timePerPercent * (100 - percentageComplete))
            
            print("Estimated time remaining: " + str(datetime.timedelta(seconds=estTimeRemaining)) + " (HH:MM:SS).")
        
        # Updates the most recent percentage of completion for comparison use
        # on the next simulation.
        lastPercentageComplete = percentageComplete
    
    # Gets the end time after the simulations have finished running.
    endTime = time.time()
    
    # All code until the next comment is for printing success / failure rates 
    # information to the console.
    successRate = (successCounter / (successCounter + failCounter)) * 100

    # Blank line before the statistics printouts start.    
    print("")
    
    # Prints failure information if any of the simulations failed.
    if failCounter > 0:
        print(str(successCounter) + " successful simulations.")
        print(str(failCounter) + " failed simulations.")
        print("Approximately " + str(int(successRate)) + "% of simulations were successful.")
        print("")
        
        # Prints failure statistics if any sim failed the green cross check,
        # otherwise prints that all sims passed the green cross check.
        if greenCrossFailCounter > 0:
            print(str(greenCrossFailCounter) + " simulations failed at the green cross check.")
            if int((greenCrossFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((greenCrossFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
        else:
            print("All simulations PASSED the green cross check.")
        
        # Prints failure statistics if any sim failed the green side check,
        # otherwise prints that all sims passed the green side check.
        if greenSideFailCounter > 0:
            print(str(greenSideFailCounter) + " simulations failed at the green side check.")
            if int((greenSideFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((greenSideFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
        else:
            print("All simulations PASSED the green side check.")
    
        # Prints failure statistics if any sim failed the aligned centers
        # check, otherwise prints that all sims passed the aligned centers
        # check.
        if alignedCentersFailCounter > 0:
            print(str(alignedCentersFailCounter) + " simulations failed at the aligned centers check.")
            if int((alignedCentersFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((alignedCentersFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
        else:
            print("All simulations PASSED the aligned centers check.")
    
        # Prints failure statistics if any sim failed the aligned corners
        # check, otherwise prints that all sims passed the aligned corners
        # check.
        if alignedCornersFailCounter > 0:
            print(str(alignedCornersFailCounter) + " simulations failed at the aligned corners check.")
            if int((alignedCornersFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((alignedCornersFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
        else:
            print("All simulations PASSED the aligned corners check.")
        
        # Prints failure statistics if any sim failed the first two rows check,
        # otherwise prints that all sims passed the first two rows check.
        if firstTwoRowsFailCounter > 0:
            print(str(firstTwoRowsFailCounter) + " simulations failed at the first two rows check.")
            if int((firstTwoRowsFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((firstTwoRowsFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
        else:
            print("All simulations PASSED the first two rows check.")
        
        # Prints failure statistics if any sim failed the blue cross check,
        # otherwise prints that all sims passed the blue cross check.
        if blueCrossFailCounter > 0:
            print(str(blueCrossFailCounter) + " simulations failed at the blue cross check.")
            if int((blueCrossFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((blueCrossFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
        else:
            print("All simulations PASSED the blue cross check.")
            
        # Prints failure statistics if any sim failed the blue side check,
        # otherwise prints that all sims passed the blue side check.
        if blueSideFailCounter > 0:
            print(str(blueSideFailCounter) + " simulations failed at the blue side check.")
            if int((blueSideFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((blueSideFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
        else:
            print("All simulations PASSED the blue side check.")
        
        # Prints failure statistics if any sim failed the top layer corners 
        # check, otherwise prints that all sims passed the top layer corners 
        # check.
        if topLayerCornersFailCounter > 0:
            print(str(topLayerCornersFailCounter) + " simulations failed at the top layer corners check.")
            if int((topLayerCornersFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((topLayerCornersFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
        else:
            print("All simulations PASSED the top layer corners check.")
            
        # Prints failure statistics if any sim failed the overall cube 
        # check, otherwise prints that all sims passed the overall cube
        # check.
        if cubeFailCounter > 0:
            print(str(cubeFailCounter) + " simulations failed at the overall cube check.")
            if int((cubeFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((cubeFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
        else:
            print("All simulations PASSED the overall cube check.")
        
    # If all sims passed all checks, does not print any of the failure info
    # to the console - just prints that all sims were successful.
    else:
        print("All " + str(numberOfSimulations) + " simulations were successful.")
    
    # Blank line to separate statistics categories.
    print("")
    
    # Time Statistics. Calculates the total time taken to run all simulations,
    # the number of simulations completed each second, and the average time
    # to complete a single simulation.
    timeTaken = endTime - startTime
    simsPerSecond = numberOfSimulations / timeTaken
    avgTimePerSim = timeTaken / numberOfSimulations
    
    print("The total time to run " + str(numberOfSimulations) + " simulations was " + str(datetime.timedelta(seconds=int(timeTaken))) + " (HH:MM:DD)")
    print("An average of around " + str(int(simsPerSecond)) + " simulations were run per second.")
    print("Average time to complete one simulation was " + str(avgTimePerSim) + " seconds.")
    
runSimulations(2000)