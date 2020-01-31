"""
Rubix Cube Solver - Solving Algorithms

v0.11 (alpha)
History available at github.com/OliverMatthews/rubiksCube/

Oli Matthews 2019
"""
# Imports relevant libraries.
import checks as chk
import cube

# Completes the 'green cross' step of solving the cube.
def solveGreenCross(cube):
    sequenceToFollow = ""
    counter = 0
    while chk.greenCross(cube.side1) != True:
        cube.followSequence(sequenceToFollow)
        sequenceToFollow = ""    
        if cube.side1[1][0] != "G":
            if cube.side2[1][0] == "G":
                sequenceToFollow = "L1"
                continue
            elif cube.side6[1][0] == "G":
                sequenceToFollow = "L2"
                continue
            elif cube.side4[1][2] == "G":
                sequenceToFollow = "L3"
                continue
            
        if cube.side1[0][1] != "G":
            if cube.side3[1][0] == "G":
                sequenceToFollow = "F1"
                continue
            elif cube.side6[2][1] == "G":
                sequenceToFollow = "F2"
                continue
            elif cube.side5[1][2] == "G":
                sequenceToFollow = "F3"
                continue
        
        if cube.side1[1][2] != "G":
            if cube.side4[1][0] == "G":
                sequenceToFollow = "R1"
                continue
            elif cube.side6[1][2] == "G":
                sequenceToFollow = "R2"
                continue
            elif cube.side2[1][2] == "G":
                sequenceToFollow = "R3"
                continue
        
        if cube.side1[2][1] != "G":
            if cube.side5[1][0] == "G":
                sequenceToFollow = "B1"
                continue
            elif cube.side6[0][1] == "G":
                sequenceToFollow = "B2"
                continue
            elif cube.side3[1][2] == "G":
                sequenceToFollow = "B3"
                continue
        
        if cube.side5[2][1] == "G":
            sequenceToFollow = "D1B1D3L3"
            continue
        elif cube.side5[0][1] == "G":
            if cube.side1[1][0] == "G":
                sequenceToFollow = "D1"
                continue
            else:
                sequenceToFollow = "L2D1B1D3L3"
                continue
        
        if cube.side4[2][1] == "G":
            if cube.side1[2][1] != "G":
                sequenceToFollow = "B1D3R1"
                continue
            else:
                sequenceToFollow = "D1"
                continue
        elif cube.side4[0][1] == "G":
            if cube.side1[1][0] == "G":
                sequenceToFollow = "D1"
                continue
            else:
                sequenceToFollow = "U2L2D1B1D3L3"
                continue
        
        if cube.side3[2][1] == "G":
            sequenceToFollow = "D2B1D3L3"
            continue
        elif cube.side3[0][1] == "G":
            if cube.side1[1][0] == "G":    
                sequenceToFollow = "D1"
                continue
            else:
                sequenceToFollow = "U3L2D1B1D3L3"
                continue
        
        if cube.side2[0][1] == "G":
            if cube.side1[1][0] == "G":
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

# Completes the 'green corners' step of solving the cube. Should only be run
# as part of the totalSolve() function, as it requires all previous solving
# steps to have been completed.
def solveGreenCorners(cube):
    sequenceToFollow = ""
    counter = 0
    errorCounter = 0
    
    while chk.greenSide(cube.side1) != True:
        cube.followSequence(sequenceToFollow)
        sequenceToFollow = ""
        
        if cube.side1[0][0] != "G":
            if cube.side2[0][0] == "G":
                sequenceToFollow = "F1U1F3"
                continue
            elif cube.side3[0][0] == "G":
                sequenceToFollow = "U1F1U1F3"
                continue
            elif cube.side4[0][0] == "G":
                sequenceToFollow = "U2F1U1F3"
                continue
            elif cube.side5[0][0] == "G":
                sequenceToFollow = "U3F1U1F3"
                continue
            
            elif cube.side6[2][0] == "G":
                sequenceToFollow = "L3U2L1U1L3U3L1"
                continue
            elif cube.side6[2][2] == "G":
                sequenceToFollow = "U1L3U2L1U1L3U3L1"
                continue
            elif cube.side6[0][2] == "G":
                sequenceToFollow = "U2L3U2L1U1L3U3L1"
                continue
            elif cube.side6[0][0] == "G":
                sequenceToFollow = "U3L3U2L1U1L3U3L1"
                continue
            
            elif cube.side4[0][2] == "G":
                sequenceToFollow = "U2L3U3L1U2L3U3L1"
                continue
            elif cube.side2[2][0] == "G":
                sequenceToFollow = "L3U1L1"
                continue
            
            elif cube.side5[2][2] == "G":
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

# Re-arranges the edge pieces neares the green side to match the colour of the
# center pieces on their respective faces. Should only be run as part of the
# totalSolve() function, as it requires all previous solution steps to have
# been completed first.
def fixAlignedCenters(cube):
    # Variables required for function to operate correctly.
    sequenceToFollow = ""
    counter = 0
    
    # Runs until the relevant edge pieces are correctly placed.
    while chk.alignedCenters(cube.side2, cube.side3, cube.side4, cube.side5) != True:
        cube.followSequence(sequenceToFollow)
        sequenceToFollow = ""
        
        # If the layer is correct but just needs rotating.
        if cube.side2[2][1] == "R" and cube.side3[2][1] == "Y" and cube.side4[2][1] == "O" and cube.side5[2][1] == "W":
            sequenceToFollow = "D1"
            continue
        elif cube.side2[2][1] == "Y" and cube.side3[2][1] == "O" and cube.side4[2][1] == "W" and cube.side5[2][1] == "R":
            sequenceToFollow = "D2"
            continue
        elif cube.side2[2][1] == "O" and cube.side3[2][1] == "W" and cube.side4[2][1] == "R" and cube.side5[2][1] == "Y":
            sequenceToFollow = "D3"
            continue
        
        # If there are two colours which need swapping.
        if cube.side5[2][1] == "Y" and cube.side4[2][1] == "O":
            sequenceToFollow = "F3B1L1F1B3U3R1L3B1R3L1U1F3B1L1F1B3"
            continue
        elif cube.side5[2][1] == "R" and cube.side3[2][1] == "O":
            sequenceToFollow = "F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif cube.side5[2][1] == "W" and cube.side2[2][1] == "O":
            sequenceToFollow = "R3L1F1L3R1U3F3B1L1F1B3U1R3L1F1L3R1"
            continue
        elif cube.side2[2][1] == "Y" and cube.side4[2][1] == "W":
            sequenceToFollow = "L1R3F1L2R2B1L2R2F1L3R1"
            continue
        elif cube.side2[2][1] == "R" and cube.side3[2][1] == "W":
            sequenceToFollow = "L1R3D1U3R3D3U1F2L3R1"
            continue
        elif cube.side4[2][1] == "R" and cube.side3[2][1] == "Y":
            sequenceToFollow = "B3F1D1U3B3U1D3R2F3B1"
            continue
        
        # If there are three colours which need rotationally swapping.
        if cube.side2[2][1] == "R" and cube.side3[2][1] == "Y" and cube.side4[2][1] == "W":
            sequenceToFollow = "L1R3F1L2R2B1L2R2F1L3R1B3F1D1U3B3U1D3R2F3B1"
            continue
        elif cube.side2[2][1] == "Y" and cube.side3[2][1] == "W" and cube.side4[2][1] == "R":
            sequenceToFollow = "L1R3D1U3R3D3U1F2L3R1B3F1D1U3B3U1D3R2F3B1"
            continue
        elif cube.side2[2][1] == "O" and cube.side3[2][1] == "W" and cube.side5[2][1] == "R":
            sequenceToFollow = "L1R3D1U3R3D3U1F2L3R1F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif cube.side2[2][1] == "R" and cube.side3[2][1] == "O" and cube.side5[2][1] == "W":
            sequenceToFollow = "R3L1F1L3R1U3F3B1L1F1B3U1R3L1F1L3R1F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif cube.side2[2][1] == "O" and cube.side4[2][1] == "W" and cube.side5[2][1] == "Y":
            sequenceToFollow = "L1R3F1L2R2B1L2R2F1L3R1F3B1L1F1B3U3R1L3B1R3L1U1F3B1L1F1B3"
            continue
        elif cube.side3[2][1] == "Y" and cube.side4[2][1] == "O" and cube.side5[2][1] == "R":
            sequenceToFollow = "F3B1L1F2B2R1F2B2L1F1B3F3B1L1F1B3U3R1L3B1R3L1U1F3B1L1F1B3"
            continue
        elif cube.side3[2][1] == "O" and cube.side4[2][1] == "R" and cube.side5[2][1] == "Y":
            sequenceToFollow = "F3B1L1F2B2R1F2B2L1F1B3B3F1D1U3B3U1D3R2F3B1"
        cube
        # Other random cases - usually specifically dealing with combinations
        # of smaller swaps.
        if cube.side2[2][1] == "R" and cube.side3[2][1] == "O" and cube.side4[2][1] == "W" and cube.side5[2][1] == "Y":
            sequenceToFollow = "L1R3F1L2R2B1L2R2F1L3R1F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif cube.side2[2][1] == "O" and cube.side3[2][1] == "W" and cube.side4[2][1] == "Y" and cube.side5[2][1] == "R":
            sequenceToFollow = "D1L1R3F1L2R2B1L2R2F1L3R1F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif cube.side2[2][1] == "W" and cube.side3[2][1] == "Y" and cube.side4[2][1] == "R" and cube.side5[2][1] == "O":
            sequenceToFollow = "D2L1R3F1L2R2B1L2R2F1L3R1F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif cube.side2[2][1] == "Y" and cube.side3[2][1] == "R" and cube.side4[2][1] == "O" and cube.side5[2][1] == "W":
            sequenceToFollow = "D3L1R3F1L2R2B1L2R2F1L3R1F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif cube.side2[2][1] == "Y" and cube.side3[2][1] == "W" and cube.side4[2][1] == "O" and cube.side5[2][1] == "R":
            sequenceToFollow = "L1R3F1L2R2B1L2R2F1L3R1L1R3D1U3R3D3U1F2L3R1F3B1L1F2B2R1F2B2L1F1B3"
            continue
        elif cube.side2[2][1] == "Y" and cube.side3[2][1] == "O" and cube.side4[2][1] == "R" and cube.side5[2][1] == "W":
            sequenceToFollow = "D1F3B1L1F2B2R1F2B2L1F1B3F3B1L1F1B3U3R1L3B1R3L1U1F3B1L1F1B3"
            continue
        elif cube.side2[2][1] == "O" and cube.side3[2][1] == "Y" and cube.side4[2][1] == "W" and cube.side5[2][1] == "R":
            sequenceToFollow = "D2F3B1L1F1B3U3R1L3B1R3L1U1F3B1L1F1B3"
            continue
        
        sequenceToFollow == "D1"
        
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break

def fixAlignedCorners(cube):
    sequenceToFollow = ""
    counter = 0
    
    while chk.alignedCorners(cube.side2, cube.side3, cube.side4, cube.side5) != True:
        cube.followSequence(sequenceToFollow)
        sequenceToFollow = ""
        
        if cube.side2[2][0] != "W" or cube.side5[2][2] != "O":
            if cube.side2[2][2] == "O" and cube.side3[2][0] == "W":
                sequenceToFollow = "R1U2R3F1U3F3U2F3U1F1"
                continue
            elif cube.side3[2][2] == "O" and cube.side4[2][0] == "W":
                sequenceToFollow = "B1U1B3U2F1U3F3U1R3U1R1"
                continue
            elif cube.side4[2][2] == "O" and cube.side5[2][0] == "W":
                sequenceToFollow = "B3U1B1F1U3F3B3U1B1"
                continue
        
        if cube.side3[2][0] != "R" or cube.side2[2][2] != "W":
            if cube.side3[2][2] == "W" and cube.side4[2][0] == "R":
                sequenceToFollow = "B1U2B3R1U3R3U1R3U2R1"
                continue
            elif cube.side4[2][2] == "W" and cube.side5[2][0] == "R":
                sequenceToFollow = "L1U1L3U2R1U3R3B3U2B1"
                continue
            
        if cube.side4[2][0] != "Y" or cube.side3[2][2] != "R":
            if cube.side4[2][2] == "R" and cube.side5[2][0] == "Y":
                sequenceToFollow = "L1U2L3B1U3B3U2B3U1B1"
                continue
            
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break


def solveFirstTwoRows(cube):
    sequenceToFollow = ""
    counter = 0
    
    while chk.firstTwoRows(cube.side2, cube.side3, cube.side4, cube.side5) != True:
        cube.followSequence(sequenceToFollow)
        sequenceToFollow = ""
        
        # If the orange and white edge piece is not correctly placed
        if cube.side2[1][0] != "W" or cube.side5[1][2] != "O":
            # If the orange and white edge piece is in the top layer
            if cube.side6[2][1] == "O" and cube.side2[0][1] == "W":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            elif cube.side6[1][2] == "O" and cube.side3[0][1] == "W":
                sequenceToFollow = "L3U1L1U1F1U3F3"
                continue
            elif cube.side6[0][1] == "O" and cube.side4[0][1] == "W":
                sequenceToFollow = "U1L3U1L1U1F1U3F3"
                continue
            elif cube.side6[1][0] == "O" and cube.side5[0][1] == "W":
                sequenceToFollow = "U2L3U1L1U1F1U3F3"
                continue
            
            # If the orange and white edge piece is inverted in the top layer.
            elif cube.side6[2][1] == "W" and cube.side2[0][1] == "O":
                sequenceToFollow = "U2F1U3F3U3L3U1L1"
                continue
            elif cube.side6[1][2] == "W" and cube.side3[0][1] == "O":
                sequenceToFollow = "U3F1U3F3U3L3U1L1"
                continue
            elif cube.side6[0][1] == "W" and cube.side4[0][1] == "O":
                sequenceToFollow = "F1U3F3U3L3U1L1"
                continue
            elif cube.side6[1][0] == "W" and cube.side5[0][1] == "O":
                sequenceToFollow = "U1F1U3F3U3L3U1L1"
                continue
            
            # If the orange and white edge piece is inverted in the correct position.
            elif cube.side2[1][0] == "O" and cube.side5[1][2] == "W":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            
            # If the orange and white edge piece is elsewhere in the middle layer.
            elif cube.side3[1][0] == "W" and cube.side2[1][2] == "O":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            elif cube.side4[1][0] == "W" and cube.side3[1][2] == "O":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            elif cube.side5[1][0] == "W" and cube.side4[1][2] == "O":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
            
            # If the orange and white edge piece is inverted elsewhere in the middle layer.
            elif cube.side3[1][0] == "O" and cube.side2[1][2] == "W":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            elif cube.side4[1][0] == "O" and cube.side3[1][2] == "W":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            elif cube.side5[1][0] == "O" and cube.side4[1][2] == "W":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
        
        # If the white and red edge piece is not correctly placed
        elif cube.side3[1][0] != "R" or cube.side2[1][2] != "W":
            # If the white and red edge piece is in the top layer
            if cube.side6[1][2] == "W" and cube.side3[0][1] == "R":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            elif cube.side6[0][1] == "W" and cube.side4[0][1] == "R":
                sequenceToFollow = "F3U1F1U1R1U3R3"
                continue
            elif cube.side6[1][0] == "W" and cube.side5[0][1] == "R":
                sequenceToFollow = "U1F3U1F1U1R1U3R3"
                continue
            elif cube.side6[2][1] == "W" and cube.side2[0][1] == "R":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            
            # If the white and red edge piece is inverted in the top layer
            elif cube.side6[1][2] == "R" and cube.side3[0][1] == "W":
                sequenceToFollow = "U2R1U3R3U3F3U1F1"
                continue
            elif cube.side6[0][1] == "R" and cube.side4[0][1] == "W":
                sequenceToFollow = "U3R1U3R3U3F3U1F1"
                continue
            elif cube.side6[1][0] == "R" and cube.side5[0][1] == "W":
                sequenceToFollow = "R1U3R3U3F3U1F1"
                continue
            elif cube.side6[2][1] == "R" and cube.side2[0][1] == "W":
                sequenceToFollow = "U1R1U3R3U3F3U1F1"
                continue
            
            # If the white and red edge piece is inverted in the correct position.
            elif cube.side3[1][0] == "W" and cube.side2[1][2] == "R":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            
            # If the white and red edge piece is elsewhere in the middle layer
            elif cube.side4[1][0] == "R" and cube.side3[1][2] == "W":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            elif cube.side5[1][0] == "R" and cube.side4[1][2] == "W":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
            elif cube.side2[1][0] == "R" and cube.side5[1][2] == "W":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            
            # If the white and red edge piece is inverted elsewhere in the middle layer
            elif cube.side4[1][0] == "W" and cube.side3[1][2] == "R":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            elif cube.side5[1][0] == "W" and cube.side4[1][2] == "R":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
            elif cube.side2[1][0] == "W" and cube.side5[1][2] == "R":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            
        # If the red and yellow edge piece is not correctly placed.
        elif cube.side4[1][0] != "Y" or cube.side3[1][2] != "R":
            # If the red and yellow edge piece is in the top layer
            if cube.side6[0][1] == "R" and cube.side4[0][1] == "Y":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            elif cube.side6[1][0] == "R" and cube.side5[0][1] == "Y":
                sequenceToFollow = "R3U1R1U1B1U3B3"
                continue
            elif cube.side6[2][1] == "R" and cube.side2[0][1] == "Y":
                sequenceToFollow = "U1R3U1R1U1B1U3B3"
                continue
            elif cube.side6[1][2] == "R" and cube.side3[0][1] == "Y":
                sequenceToFollow = "U2R3U1R1U1B1U3B3"
                continue
            
            # If the red and yellow edge piece is inverted in the top layer
            elif cube.side6[0][1] == "Y" and cube.side4[0][1] == "R":
                sequenceToFollow = "U1B1U3B3U3R3U1R1"
                continue
            elif cube.side6[1][0] == "Y" and cube.side5[0][1] == "R":
                sequenceToFollow = "U2B1U3B3U3R3U1R1"
                continue
            elif cube.side6[2][1] == "Y" and cube.side2[0][1] == "R":
                sequenceToFollow = "U3B1U3B3U3R3U1R1"
                continue
            elif cube.side6[1][2] == "Y" and cube.side3[0][1] == "R":
                sequenceToFollow = "B1U3B3U3R3U1R1"
                continue
            
            # If the red and yellow edge piece is inverted in the correct position
            elif cube.side4[1][0] == "R" and cube.side3[1][2] == "Y":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            
            # If the red and yellow edge piece is elsewhere in the middle layer
            elif cube.side5[1][0] == "Y" and cube.side4[1][2] == "R":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
            elif cube.side2[1][0] == "Y" and cube.side5[1][2] == "R":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            elif cube.side3[1][0] == "Y" and cube.side2[1][2] == "R":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            
            # If the red and yellow edge piece is inverted elsewhere in the middle layer
            elif cube.side5[1][0] == "R" and cube.side4[1][2] == "Y":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
            elif cube.side2[1][0] == "R" and cube.side5[1][2] == "Y":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            elif cube.side3[1][0] == "R" and cube.side2[1][2] == "Y":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
        
        # If the yellow and orange edge piece is not correctly placed.
        elif cube.side5[1][0] != "O" or cube.side4[1][2] != "Y":
            # If the yellow and orange edge piece is in the top layer
            if cube.side6[1][0] == "Y" and cube.side5[0][1] == "O":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
            elif cube.side6[2][1] == "Y" and cube.side2[0][1] == "O":
                sequenceToFollow = "B3U1B1U1L1U3L3"
                continue
            elif cube.side6[1][2] == "Y" and cube.side3[0][1] == "O":
                sequenceToFollow = "U1B3U1B1U1L1U3L3"
                continue
            elif cube.side6[0][1] == "Y" and cube.side4[0][1] == "O":
                sequenceToFollow = "U2B3U1B1U1L1U3L3"
                continue
            
            # If the yellow and orange edge piece is inverted in the top layer
            elif cube.side6[1][0] == "O" and cube.side5[0][1] == "Y":
                sequenceToFollow = "U2L1U3L3U3B3U1B1"
                continue
            elif cube.side6[2][1] == "O" and cube.side2[0][1] == "Y":
                sequenceToFollow = "U3L1U3L3U3B3U1B1"
                continue
            elif cube.side6[1][2] == "O" and cube.side3[0][1] == "Y":
                sequenceToFollow = "L1U3L3U3B3U1B1"
                continue
            elif cube.side6[0][1] == "O" and cube.side4[0][1] == "Y":
                sequenceToFollow = "U1L1U3L3U3B3U1B1"
                continue
            
            # If the yellow and orange edge piece is inverted in the correct position.
            elif cube.side5[1][0] == "Y" and cube.side4[1][2] == "O":
                sequenceToFollow = "U3B3U1B1U1L1U3L3"
                continue
            
            # If the yellow and orange edge piece is elsewhere in the middle layer
            elif cube.side2[1][0] == "O" and cube.side5[1][2] == "Y":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            elif cube.side3[1][0] == "O" and cube.side2[1][2] == "Y":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            elif cube.side4[1][0] == "O" and cube.side3[1][2] == "Y":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            
            # If the yellow and orange edge piece is elsewhere in the middle layer
            elif cube.side2[1][0] == "Y" and cube.side5[1][2] == "O":
                sequenceToFollow = "U3L3U1L1U1F1U3F3"
                continue
            elif cube.side3[1][0] == "Y" and cube.side2[1][2] == "O":
                sequenceToFollow = "U3F3U1F1U1R1U3R3"
                continue
            elif cube.side4[1][0] == "Y" and cube.side3[1][2] == "O":
                sequenceToFollow = "U3R3U1R1U1B1U3B3"
                continue
            
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break

# Function for solving the 'blue cross' step of the cube. Should only be run
# as part of the totalSolve() function, as it will not work unless all previous
# solution steps have been completed.
def solveBlueCross(cube):
    # Sets up variables for function to operate correctly.
    counter = 0
    sequenceToFollow = ""
    
    # Runs until the blue cross is formed.
    while chk.blueCross(cube.side6) != True:
        # Follows the sequence from the last run of the loop, then clears the
        # sequence string ready for the next instruction.
        cube.followSequence(sequenceToFollow)
        sequenceToFollow = ""
        
        # Gets the number of correctly positioned blue pieces. Used to decide
        # what state the cube is already in.
        numberOfCorrectBlue = 0
        if cube.side6[0][1] == "B":
            numberOfCorrectBlue += 1
        if cube.side6[1][0] == "B":
            numberOfCorrectBlue += 1
        if cube.side6[1][2] == "B":
            numberOfCorrectBlue += 1
        if cube.side6[2][1] == "B":
            numberOfCorrectBlue += 1
    
        # If no blue edge pieces are in the correct place
        if numberOfCorrectBlue == 0:
            sequenceToFollow = "F1U1R1U3R3F3"
            continue
        
        # If two of the blue edge pieces are in the correct place
        elif numberOfCorrectBlue == 2:
            # If the two blue edge pieces form a 'V' shape
            if cube.side6[0][1] == "B" and cube.side6[1][0] == "B":
                sequenceToFollow = "F1U1R1U3R3F3"
                continue
            elif cube.side6[1][0] == "B" and cube.side6[2][1] == "B":
                sequenceToFollow = "U1F1U1R1U3R3F3"
                continue
            elif cube.side6[2][1] == "B" and cube.side6[1][2] == "B":
                sequenceToFollow = "U2F1U1R1U3R3F3"
                continue
            elif cube.side6[1][2] == "B" and cube.side6[0][1] == "B":
                sequenceToFollow = "U3F1U1R1U3R3F3"
                continue
            
            # If the two blue edge pieces form a horizontal line
            elif cube.side6[1][0] == "B" and cube.side6[1][2] == "B":
                sequenceToFollow = "F1R1U1R3U3F3"
                continue
            elif cube.side6[0][1] == "B" and cube.side6[2][1] == "B":
                sequenceToFollow = "U1F1R1U1R3U3F3"
                continue
        
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break

def solveBlueSide(cube):
    counter = 0
    sequenceToFollow = ""
    
    while chk.blueSide(cube.side6) != True:
        cube.followSequence(sequenceToFollow)
        sequenceToFollow = ""
        
        numberOfCorrectBlue = 0
        if cube.side6[0][0] == "B":
            numberOfCorrectBlue += 1
        if cube.side6[0][2] == "B":
            numberOfCorrectBlue += 1
        if cube.side6[2][0] == "B":
            numberOfCorrectBlue += 1
        if cube.side6[2][2] == "B":
            numberOfCorrectBlue += 1
        
        if numberOfCorrectBlue == 0:
            if cube.side5[0][2] != "B":
                sequenceToFollow = "U1"
                continue
            else:
                sequenceToFollow = "R1U1R3U1R1U2R3"
                continue
            
        if numberOfCorrectBlue == 1:
            if cube.side6[2][0] != "B":
                sequenceToFollow = "U1"
                continue
            else:
                sequenceToFollow = "R1U1R3U1R1U2R3"
                continue
                
        elif numberOfCorrectBlue == 2:
            if cube.side2[0][0] != "B":
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
def solveTopLayerCorners(cube):
    # Sets up variables for function to operate correctly.
    counter = 0
    sequenceToFollow = ""
    
    # Runs until the top layer corners are in the correct position.
    while chk.topLayerCorners(cube.side2, cube.side3, cube.side4, cube.side5) != True:
        cube.followSequence(sequenceToFollow)
        sequenceToFollow = ""
        
        # Gets the number of correctly positioned corner pieces. Used to decide
        # what state the cube is already in.
        numberOfCorrectCorners = 0
        if cube.side2[0][0] == "W" and cube.side5[0][2] == "O":
            numberOfCorrectCorners += 1
        if cube.side3[0][0] == "R" and cube.side2[0][2] == "W":
            numberOfCorrectCorners += 1
        if cube.side4[0][0] == "Y" and cube.side3[0][2] == "R":
            numberOfCorrectCorners += 1
        if cube.side5[0][0] == "O" and cube.side4[0][2] == "Y":
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
            if (cube.side2[0][0] == "W" and cube.side5[0][2] == "O") and (cube.side4[0][0] == "Y" and cube.side3[0][2] == "R"):
                sequenceToFollow = "R3F1R3B2R1F3R3B2R2U3"
                continue
            elif (cube.side3[0][0] == "R" and cube.side2[0][2] == "W") and (cube.side5[0][0] == "O" and cube.side4[0][2] == "Y"):
                sequenceToFollow = "R3F1R3B2R1F3R3B2R2U3"
                continue
            
            # When the two correct pieces include the same face of the cube.
            elif (cube.side4[0][0] == "Y" and cube.side3[0][2] == "R") and (cube.side5[0][0] == "O" and cube.side4[0][2] == "Y"):
                sequenceToFollow = "R3F1R3B2R1F3R3B2R2U3"
                continue
            elif (cube.side2[0][0] == "W" and cube.side5[0][2] == "O") and (cube.side5[0][0] == "O" and cube.side4[0][2] == "Y"):
                sequenceToFollow = "B3R1B3L2B1R3B3L2B2U3"
                continue
            elif (cube.side3[0][0] == "R" and cube.side2[0][2] == "W") and (cube.side2[0][0] == "W" and cube.side5[0][2] == "O"):
                sequenceToFollow = "L3B1L3F2L1B3L3F2L2U3"
                continue
            elif (cube.side4[0][0] == "Y" and cube.side3[0][2] == "R") and (cube.side3[0][0] == "R" and cube.side2[0][2] == "W"):
                sequenceToFollow = "F3L1F3R2F1L3F3R2F2U3"
                continue
            
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break
        
# Function for solving the top layer edges of the cube. Should only be run as
# part of the totalSolve() function, as it will not work unless all previous
# solution steps have been completed.
def solveTopLayerEdges(cube):
    # Sets up variables for function to operate correctly.
    counter = 0
    sequenceToFollow = ""

    # Runs until the cube is solved.
    while chk.wholeCube(cube.side1, cube.side2, cube.side3, cube.side4, cube.side5, cube.side6) != True:
        cube.followSequence(sequenceToFollow)
        sequenceToFollow = ""
    
        # Gets the number of correctly positioned edge pieces. Used to decide
        # what state the cube is already in.
        numberOfCorrectEdges = 0
        if cube.side2[0][1] == "G":
            numberOfCorrectEdges += 1
        if cube.side3[0][1] == "R":
            numberOfCorrectEdges += 1
        if cube.side4[0][1] == "Y":
            numberOfCorrectEdges += 1
        if cube.side5[0][1] == "O":
            numberOfCorrectEdges += 1
        
        # If no edges are correctly positioned, run the sequence anyway and
        # within 2 iterations of the loop one should be in the correct spot.
        if numberOfCorrectEdges == 0:
            sequenceToFollow = "F2U1L1R3F2L3R1U1F2"
            continue
        
        # Otherwise find and run the correct algorithm.
        elif numberOfCorrectEdges == 1:
            # If the red top edge piece is correct.
            if cube.side3[0][1] == "R":
                sequenceToFollow = "L2U1B1F3L2B3F1U1L2"
                continue
            
            # If the yellow top edge piece is correct.
            elif cube.side4[0][1] == "Y":
                sequenceToFollow = "F2U1L1R3F2L3R1U1F2"
                continue
            
            # If the orange top edge piece is correct.
            elif cube.side5[0][1] == "O":
                sequenceToFollow = "R2U1F1B3R2F3B1U1R2"
                continue
            
            # If the white top edge piece is correct.
            elif cube.side6[0][1] == "W":
                sequenceToFollow = "B2U1R1L3B2R3L1U1B2"
                continue
            
        # Standard failsafe, breaks out of function if it gets stuck in a loop
        counter += 1
        if counter > 10:
            break
        
# Calls each of the solving functions in order, completely solving the cube!
def totalSolve(cube):
    solveGreenCross(cube)
    solveGreenCorners(cube)
    fixAlignedCenters(cube)
    fixAlignedCorners(cube)
    solveFirstTwoRows(cube)
    solveBlueCross(cube)
    solveBlueSide(cube)
    solveTopLayerCorners(cube)
    solveTopLayerEdges(cube)
