"""
Rubix Cube Solver - Cube State Checking Algorithms

v0.5 (alpha)
History available at github.com/OliverMatthews/rubiksCube/

Oli Matthews 2019
"""
# Checks whether the 'green cross' step has been completed correctly. Takes one
# side matrix as input.
def greenCross(side):
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
def greenSide(side):
    
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
def alignedCenters(side2, side3, side4, side5):
    
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
def alignedCorners(side2, side3, side4, side5):
    
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
def firstTwoRows(side2, side3, side4, side5):
    
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
def blueCross(side):
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
def blueSide(side):
    
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
def topLayerCorners(side2, side3, side4, side5):
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
    
def wholeCube(side1, side2, side3, side4, side5, side6):
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