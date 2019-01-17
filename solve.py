"""
Rubix Cube Solver - Solving Algorithms

v0.5 (alpha)
History available at github.com/OliverMatthews/rubiksCube/

Oli Matthews 2019
"""
# Imports relevant libraries.
import checks as chk
import cube

# Initialises the game cube from the rubikCube class with a cube size of 3.
a = cube.rubikCube(3)

def solveGreenCross():
    sequenceToFollow = ""
    counter = 0
    while chk.greenCross(a.side1) != True:
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
    
    while chk.greenSide(a.side1) != True:
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
    
    while chk.alignedCenters(a.side2, a.side3, a.side4, a.side5) != True:
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
    
    while chk.alignedCorners(a.side2, a.side3, a.side4, a.side5) != True:
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
    
    while chk.firstTwoRows(a.side2, a.side3, a.side4, a.side5) != True:
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
    while chk.blueCross != True:
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
    
    while chk.blueSide(a.side6) != True:
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
    while chk.topLayerCorners(a.side2, a.side3, a.side4, a.side5) != True:
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
    while chk.wholeCube(a.side1, a.side2, a.side3, a.side4, a.side5, a.side6) != True:
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