"""
Rubix Cube Solver - Face Rotation Algorithms

v0.9 (alpha)
History available at github.com/OliverMatthews/rubiksCube/

Oli Matthews 2019
"""

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
        colourSequence = colourSequence[-cubeSize:] + colourSequence[:-cubeSize]
        return colourSequence
    
# Uses matrix manipulation to rotate a side without changing the order of the
# colours in any way.
def rotateStillFace(side, inverse):
    # Rotates the input matrix by 90 degrees, clockwise.
    if inverse == False:
        for i in range(len(side)):
            for j in range(i, len(side)):
                temp = side[j][i]
                side[j][i] = side[i][j]
                side[i][j] = temp
        
        for i in range(len(side)): 
            j = 0
            k = len(side)-1
            while j < k: 
                temp = side[i][j] 
                side[i][j] = side[i][k] 
                side[i][k] = temp 
                j += 1
                k -= 1
                
        return side
    
    # Rotates the input matrix by 90 degrees, anticlockwise. Used for inverse
    # rotations.
    elif inverse == True:
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
def rotateLeft(side1, side2, side6, side4, side5, inverse):
    colourSequence = ""
    
    for i in range(len(side1)-1, -1, -1):
        colourSequence = colourSequence + side1[i][0]
    
    for i in range(len(side2)-1, -1, -1):
        colourSequence = colourSequence + side2[i][0]
        
    for i in range(len(side6)-1, -1, -1):
        colourSequence = colourSequence + side6[i][0]
        
    for i in range(len(side4)):
        colourSequence = colourSequence + side4[i][2]
    
    colourSequence = shiftColourSequence(len(side1), colourSequence, inverse)
    
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
    
    side5 = rotateStillFace(side5, False)
            
    return side1, side2, side6, side4, side5

# Rotates the 'right' face of the cube clockwise 90 degrees.
def rotateRight(side1, side2, side6, side4, side3, inverse):
    colourSequence = ""
    
    for i in range(len(side6)):
        colourSequence = colourSequence + side6[i][2]
    
    for i in range(len(side2)):
        colourSequence = colourSequence + side2[i][2]
    
    for i in range(len(side1)):
        colourSequence = colourSequence + side1[i][2]
    
    for i in range(len(side4)-1, -1, -1):
        colourSequence = colourSequence + side4[i][0]

    colourSequence = shiftColourSequence(len(side1), colourSequence, inverse)

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
    
    side3 = rotateStillFace(side3, False)
    
    return side1, side2, side6, side4, side3

# Rotates the 'up' face of the cube clockwise 90 degrees.
def rotateUp(side2, side3, side4, side5, side6, inverse):
    colourSequence = ""
    
    for i in range(len(side2)):
        colourSequence = colourSequence + side2[0][i]
    
    for i in range(len(side3)):
        colourSequence = colourSequence + side3[0][i]
    
    for i in range(len(side4)):
        colourSequence = colourSequence + side4[0][i]
    
    for i in range(len(side5)):
        colourSequence = colourSequence + side5[0][i]
    
    colourSequence = shiftColourSequence(len(side2), colourSequence, inverse)
    
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
    
    side6 = rotateStillFace(side6, False)
    
    return side2, side3, side4, side5, side6

# Rotates the 'down' face of the cube clockwise 90 degrees.
def rotateDown(side2, side3, side4, side5, side1, inverse):
    colourSequence = ""
    
    for i in range(len(side2)-1, -1, -1):
        colourSequence = colourSequence + side2[2][i]
    
    for i in range(len(side5)-1, -1, -1):
        colourSequence = colourSequence + side5[2][i]
    
    for i in range(len(side4)-1, -1, -1):
        colourSequence = colourSequence + side4[2][i]
    
    for i in range(len(side3)-1, -1, -1):
        colourSequence = colourSequence + side3[2][i]
    
    colourSequence = shiftColourSequence(len(side2), colourSequence, inverse)
    
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
        
    side1 = rotateStillFace(side1, False)
    
    return side2, side3, side4, side5, side1

# Rotates the 'front' face of the cube clockwise 90 degrees.
def rotateFront(side1, side3, side6, side5, side2, inverse):
    colourSequence = ""
    
    for i in range(len(side1)):
        colourSequence = colourSequence + side1[0][i]
    
    for i in range(len(side3)-1, -1, -1):
        colourSequence = colourSequence + side3[i][0]
    
    for i in range(len(side6)-1, -1, -1):
        colourSequence = colourSequence + side6[2][i]
    
    for i in range(len(side5)):
        colourSequence = colourSequence + side5[i][2]
    
    colourSequence = shiftColourSequence(len(side1), colourSequence, inverse)
    
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
    
    side2 = rotateStillFace(side2, False)
    
    return side1, side3, side6, side5, side2

# Rotates the 'back' face of the cube clockwise 90 degrees.
def rotateBack(side1, side5, side6, side3, side4, inverse):
    colourSequence = ""
    
    for i in range(len(side1)-1, -1, -1):
        colourSequence = colourSequence + side1[2][i]
        
    for i in range(len(side5)-1, -1, -1):
        colourSequence = colourSequence + side5[i][0]
    
    for i in range(len(side6)):
        colourSequence = colourSequence + side6[0][i]
    
    for i in range(len(side3)):
        colourSequence = colourSequence + side3[i][2]
    
    colourSequence = shiftColourSequence(len(side1), colourSequence, inverse)
    
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
    
    side4 = rotateStillFace(side4, False)
    
    return side1, side5, side6, side3, side4