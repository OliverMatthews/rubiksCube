"""
Rubix Cube Solver - Developer Functions

v0.11 (alpha)
History available at github.com/OliverMatthews/rubiksCube/

Oli Matthews 2019
"""
# Imports relevant libraries
import solve
from multiprocessing import Pool
import psutil
import time
import datetime
import platform
from tqdm import tqdm

# Class contains developer mode settings which can be toggled on or off
class devFunctions:
    # Initialises the settings and sets the default state for each toggle.
    def __init__(self):
        self.sequencePrinting = False
        self.simFailStatsPrinting = True
        self.finalTimeStatsPrinting = True
        self.saveSolutions = False
    
    # Toggles whether all sequences followed should be printed to the console.
    # Default state for this is OFF.    
    def toggleSequencePrinting(self, boolean):
        if boolean == True:
            self.sequencePrinting = True
            print("DEV: Sequence printing is now ON!")
        elif boolean == False:
            self.sequencePrinting = False
            print("DEV: Sequence printing is now OFF! (this is the default state)")
    
    # Toggles whether statistics pertaining to the pass/fail rate of 
    # simulations should be collected and printed to the console. Default state
    # for this is OFF.
    def toggleSimFailStatsPrinting(self, boolean):
        if boolean == True:
            self.simFailStatsPrinting = True
            print("DEV: Simulation pass/fail statistics printing is now ON!")
        elif boolean == False:
            self.simFailStatsPrinting = False
            print("DEV: Simulation pass/fail statistics printing is now OFF! (this is the default state)")
    
    # Toggles whether statistics pertaining to overall time taken for
    # simulations to run should be collected and printed to the console.
    # Default state for this is ON.
    def toggleFinalTimeStatsPrinting(self, boolean):
        if boolean == True:
            self.finalTimeStatsPrinting = True
            print("DEV: Simulation final time statistics printing is now ON! (this is the default state)")
        elif boolean == False:
            self.finalTimeStatsPrinting = True
            print("DEV: Simulation final time statistics printing is now OFF!")
            
    # Toggles whether the initial cube state and the sequence followed to solve
    # that cube should be saved to a log file. Default state for this is OFF.
    def toggleSaveSolutions(self, boolean):
        if boolean == True:
            self.saveSolutions = True
            print("DEV: Cube data and solution steps logging is now ON!")
        elif boolean == False:
            self.saveSolutions = False
            print("DEV: Cube data and solution steps logging is now OFF! (this is the default state)")
            
# Intitialises the dev mode settings for use.
devSettings = devFunctions()

# Function to run a single simulation.
def runSimulation(simNumber):
    # Initialises a new cube.
    gameCube = solve.cube.rubikCube(3)

    # Randomly shuffles the cube 30 times - enough to ensure a random shuffle,
    # then saves the layout of the cube (if sequence logging is enabled in the)
    # developer settings.
    gameCube.randomShuffle(30)
    if devSettings.saveSolutions == True:
        gameCube.saveCurrentLayout()

    # Runs the solving procedure on the cube.
    solve.totalSolve(gameCube)

    # Saves the complete sequence of moves used to solve the cube, if sequence
    # logging is enabled in the developer settings.
    if devSettings.saveSolutions == True:
        logSolution((simNumber + 1), gameCube)

    # Checks that the cube has been completed correctly. Returns false if the
    # cube was not solved, and returns true if the cube was solved.
    if solve.chk.wholeCube(gameCube.side1, gameCube.side2, gameCube.side3, gameCube.side4, gameCube.side5, gameCube.side6) == False:
        if solve.chk.greenCross(gameCube.side1) == False:
            return "GC"
        elif solve.chk.greenSide(gameCube.side1) == False:
            return "GS"
        elif solve.chk.alignedCenters(gameCube.side2, gameCube.side3, gameCube.side4, gameCube.side5) == False:
            return "ACE"
        elif solve.chk.alignedCorners(gameCube.side2, gameCube.side3, gameCube.side4, gameCube.side5) == False:
            return "ACO"
        elif solve.chk.firstTwoRows(gameCube.side2, gameCube.side3, gameCube.side4, gameCube.side5) == False:
            return "FTR"
        elif solve.chk.blueCross(gameCube.side6) == False:
            return "BC"
        elif solve.chk.blueSide(gameCube.side6) == False:
            return "BS"
        elif solve.chk.topLayerCorners(gameCube.side2, gameCube.side3, gameCube.side4, gameCube.side5) == False:
            return "TLC"
    else:
        return True

# Function to run many simulations. Each simulation randomly shuffles the cube,
# solves it, and checks the end state of the cube is correctly solved. After
# running all simulations, prints information indicating various statistics
# such as pass/fail count and time taken. Does not work on Windows.
def runManySimulations(numberOfSimulations):
    # Marks the starting time.
    startTime = time.time()

    # Gets the number of real (not logical) CPU cores. If "None" is returned,
    # assumes a single core to be safe.
    if psutil.cpu_count(logical=False) == "None":
        cores = 1
    else:
        cores = int(psutil.cpu_count(logical=False))

    # Initialises the results list.
    res = []

    # Initialises as many processes as there are real (not logical) CPU cores
    # as a pool, then uses the pool to complete all simulations. Keeps track
    # of how many passes and fails there were in the 'res' list. A progress
    # bar is shown whilst running simulations, as a large number of simulations
    # can take some time to complete. Multi-core processing is disabled on
    # machines running Windows.
    if platform.system() == "Windows":
        print("Please be aware multi-core processing is currently unavailable on Windows.")
        with tqdm(total=numberOfSimulations) as progressBar:
            for i in tqdm(range(numberOfSimulations)):
                res.append((runSimulation(i)))
                progressBar.update()
    else:
        with Pool(processes=cores) as pool:
            with tqdm(total=numberOfSimulations) as progressBar:
                for i, result in tqdm(enumerate(pool.imap(runSimulation, range(numberOfSimulations)))):
                    progressBar.update()
                    res.append(result)
    
    # Marks the end time and calculates the time taken to run all simulations
    endTime = time.time()

    # Prints out pass/fail statistics if the relevant setting is enabled.
    if devSettings.simFailStatsPrinting == True:
        # Calculates the pass/fail rate.
        passCount, failCountArray = passFailCount(res)
        failCount = failCountArray[0]
        successRate = (passCount / (passCount + failCount)) * 100

        # Unpacks the values from the fail counters.
        greenCrossFailCounter = failCountArray[1]
        greenSideFailCounter = failCountArray[2]
        alignedCentersFailCounter = failCountArray[3]
        alignedCornersFailCounter = failCountArray[4]
        firstTwoRowsFailCounter = failCountArray[5]
        blueCrossFailCounter = failCountArray[6]
        blueSideFailCounter = failCountArray[7]
        topLayerCornersFailCounter = failCountArray[8]

        # Prints failure information if any of the simulations failed.
        if failCount > 0:
            print(str(passCount) + " successful simulations.")
            print(str(failCount) + " failed simulations.")
            print("Approximately " + str(int(successRate)) + "% of simulations passed.")
            print("")
        # If all simulations passed all checks, just prints that all
        # simulations were successful.
        else:
            print("All " + str(numberOfSimulations) + " simulations passed.")

        # Prints failure statistics if any sim failed the green cross check,
        # otherwise prints that all sims passed the green cross check.
        if greenCrossFailCounter > 0:
            print(str(greenCrossFailCounter) + " simulations failed at the green cross check.")
            if int((greenCrossFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((greenCrossFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
        
        # Prints failure statistics if any sim failed the green side check,
        # otherwise prints that all sims passed the green side check.
        if greenSideFailCounter > 0:
            print(str(greenSideFailCounter) + " simulations failed at the green side check.")
            if int((greenSideFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((greenSideFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
    
        # Prints failure statistics if any sim failed the aligned centers
        # check, otherwise prints that all sims passed the aligned centers
        # check.
        if alignedCentersFailCounter > 0:
            print(str(alignedCentersFailCounter) + " simulations failed at the aligned centers check.")
            if int((alignedCentersFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((alignedCentersFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
    
        # Prints failure statistics if any sim failed the aligned corners
        # check, otherwise prints that all sims passed the aligned corners
        # check.
        if alignedCornersFailCounter > 0:
            print(str(alignedCornersFailCounter) + " simulations failed at the aligned corners check.")
            if int((alignedCornersFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((alignedCornersFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
        
        # Prints failure statistics if any sim failed the first two rows check,
        # otherwise prints that all sims passed the first two rows check.
        if firstTwoRowsFailCounter > 0:
            print(str(firstTwoRowsFailCounter) + " simulations failed at the first two rows check.")
            if int((firstTwoRowsFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((firstTwoRowsFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
        
        # Prints failure statistics if any sim failed the blue cross check,
        # otherwise prints that all sims passed the blue cross check.
        if blueCrossFailCounter > 0:
            print(str(blueCrossFailCounter) + " simulations failed at the blue cross check.")
            if int((blueCrossFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((blueCrossFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
            
        # Prints failure statistics if any sim failed the blue side check,
        # otherwise prints that all sims passed the blue side check.
        if blueSideFailCounter > 0:
            print(str(blueSideFailCounter) + " simulations failed at the blue side check.")
            if int((blueSideFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((blueSideFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
        
        # Prints failure statistics if any sim failed the top layer corners 
        # check, otherwise prints that all sims passed the top layer corners 
        # check.
        if topLayerCornersFailCounter > 0:
            print(str(topLayerCornersFailCounter) + " simulations failed at the top layer corners check.")
            if int((topLayerCornersFailCounter / numberOfSimulations)*100) > 1:
                print("This represents approximately " + str(int((topLayerCornersFailCounter / numberOfSimulations)*100)) + "% of the simulations run.")
            else:
                print("This represents less than 1% of the simulations run.")
        
        # Blank line to separate statistics categories.
        print("")

    # Only prints out final time statistics if the relevant setting is enabled.
    if devSettings.finalTimeStatsPrinting == True:
        # Time Statistics. Calculates the total time taken to run all simulations,
        # the number of simulations completed each second, and the average time
        # to complete a single simulation.
        timeTaken = endTime - startTime
        simsPerSecond = numberOfSimulations / timeTaken
        avgTimePerSim = timeTaken / numberOfSimulations
        
        # Prints time statistics.
        print("The total time to run " + str(numberOfSimulations) + " simulations was " + str(datetime.timedelta(seconds=int(timeTaken))) + " (HH:MM:DD)")
        print("An average of around " + str(int(simsPerSecond)) + " simulations were run per second.")
        print("Average time to complete one simulation was " + str(avgTimePerSim) + " seconds.")

# Converts the results list into a count of passed vs failed simulations.
def passFailCount(resultsList):
    # Initialises the pass and fail counters.
    passCounter = 0
    failCounter = 0

    # Initialises the fail counters by type of failure.
    greenCrossFailCounter = 0
    greenSideFailCounter = 0
    alignedCentersFailCounter = 0
    alignedCornersFailCounter = 0
    firstTwoRowsFailCounter = 0
    blueCrossFailCounter = 0
    blueSideFailCounter = 0
    topLayerCornersFailCounter = 0

    # Cycles through the results, and increments either the pass or fail
    # counter depending on whether the simulation passed or failed.
    for i in resultsList:
        if i == "GC":
            failCounter += 1
            greenCrossFailCounter += 1
        elif i == "GS":
            failCounter += 1
            greenSideFailCounter += 1
        elif i == "ACE":
            failCounter += 1
            alignedCentersFailCounter += 1
        elif i == "ACO":
            failCounter += 1
            alignedCornersFailCounter += 1
        elif i == "FTR":
            failCounter += 1
            firstTwoRowsFailCounter += 1
        elif i == "BC":
            failCounter += 1
            blueCrossFailCounter += 1
        elif i == "BS":
            failCounter += 1
            blueSideFailCounter += 1
        elif i == "TLC":
            failCounter += 1
            topLayerCornersFailCounter += 1
        else:
            passCounter += 1
    
    # Packs all the failure types into a single array.
    failCounterArray = [failCounter, greenCrossFailCounter, greenSideFailCounter, alignedCentersFailCounter, alignedCornersFailCounter, firstTwoRowsFailCounter, blueCrossFailCounter, blueSideFailCounter, topLayerCornersFailCounter]

    # Returns the pass counter and failure counter array.
    return passCounter, failCounterArray

def logSolution(simNo, cube):
    # Unpacks the saved layout of the cube into 6 separate side matrices.
    side1 = cube.layout[0]
    side2 = cube.layout[1]
    side3 = cube.layout[2]
    side4 = cube.layout[3]
    side5 = cube.layout[4]
    side6 = cube.layout[5]
    completeSequence = sequenceSpacer(cube.sequenceLog)

    textToWrite = ""

    textToWrite = textToWrite + "*** SIMULATION NUMBER " + str(simNo) + " ***" + "\n" + "Cube starting state: "
    
    textToWrite = textToWrite + "\n" + "Side 1: "
    for i in range(cube.cubeSize):
        textToWrite = textToWrite + "\n"
        for j in range(cube.cubeSize):
            textToWrite = textToWrite + side1[i][j] + " "
    
    textToWrite = textToWrite + "\n" + "Side 2: "
    for i in range(cube.cubeSize):
        textToWrite = textToWrite + "\n"
        for j in range(cube.cubeSize):
            textToWrite = textToWrite + side2[i][j] + " "
            
    textToWrite = textToWrite + "\n" + "Side 3: "
    for i in range(cube.cubeSize):
        textToWrite = textToWrite + "\n"
        for j in range(cube.cubeSize):
            textToWrite = textToWrite + side3[i][j] + " "
            
    textToWrite = textToWrite + "\n" + "Side 4: "
    for i in range(cube.cubeSize):
        textToWrite = textToWrite + "\n"
        for j in range(cube.cubeSize):
            textToWrite = textToWrite + side4[i][j] + " "
            
    textToWrite = textToWrite + "\n" + "Side 5: "
    for i in range(cube.cubeSize):
        textToWrite = textToWrite + "\n"
        for j in range(cube.cubeSize):
            textToWrite = textToWrite + side5[i][j] + " "
            
    textToWrite = textToWrite + "\n" + "Side 6: "
    for i in range(cube.cubeSize):
        textToWrite = textToWrite + "\n"
        for j in range(cube.cubeSize):
            textToWrite = textToWrite + side6[i][j] + " "

    textToWrite = textToWrite + "\n" + str(int(len(cube.sequenceLog)/2)) + " moves were taken to complete this cube."
    textToWrite = textToWrite + "\n" + "Solution sequence: " + "\n" + completeSequence + "\n" + "\n"

    file = open("sequenceLog.txt", "a")
    file.write(textToWrite)
    file.close()

# This function puts a comma and a space between each move in a given sequence.
def sequenceSpacer(sequence):
    # Sets the output sequence to be empty.
    spacedSequence = ""
    
    # Repeatedly gets the next move from the sequence and inserts a comma and a
    # space.
    for i in range(int(len(sequence)/2)):
        # Checks if there are still more moves in the sequence. If there are,
        # the move is formatted with a comma and a space after it. If it is the
        # last move in the sequence, the move is formatted with just a period.
        if int(len(sequence)) > 2:
            spacedSequence = spacedSequence + str(sequence[0:2]) + ", "
            sequence = sequence[2:]
        else: 
            spacedSequence = spacedSequence + str(sequence[0:2]) + "."
            sequence = ""

    # Returns the sequence with commas and spaces.
    return spacedSequence