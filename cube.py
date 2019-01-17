"""
Rubix Cube Solver - Cube Object(s)

v0.6 (alpha)
History available at github.com/OliverMatthews/rubiksCube/

Oli Matthews 2019
"""
# Imports relevant libraries.
from random import randint
import rotations as rt

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
                self.side1, self.side2, self.side6, self.side4, self.side5 = rt.rotateLeft(self.side1, self.side2, self.side6, self.side4, self.side5)
        
        # Given 'R' as input, rotates the right face by a given number of turns.
        elif face == "R":
            for i in range(turns):
                self.side1, self.side2, self.side6, self.side4, self.side3 = rt.rotateRight(self.side1, self.side2, self.side6, self.side4, self.side3)
        
        # Given 'U' as input, rotates the up face by a given number of turns.
        elif face == "U":
            for i in range(turns):
                self.side2, self.side3, self.side4, self.side5, self.side6 = rt.rotateUp(self.side2, self.side3, self.side4, self.side5, self.side6)

        # Given 'D' as input, rotates the down face by a given number of turns.
        elif face == "D":
            for i in range(turns):
                self.side2, self.side3, self.side4, self.side5, self.side1 = rt.rotateDown(self.side2, self.side3, self.side4, self.side5, self.side1)
        
        # Given 'F' as input, rotates the front face by a given number of turns.
        elif face == "F":
            for i in range(turns):
                self.side1, self.side3, self.side6, self.side5, self.side2 = rt.rotateFront(self.side1, self.side3, self.side6, self.side5, self.side2)
        
        # Given 'B' as input, rotates the back face by a given number of turns.
        elif face == "B":
            for i in range(turns):
                self.side1, self.side5, self.side6, self.side3, self.side4 = rt.rotateBack(self.side1, self.side5, self.side6, self.side3, self.side4)
    
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