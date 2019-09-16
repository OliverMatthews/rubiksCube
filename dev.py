"""
Rubix Cube Solver - Developer Functions

v0.11 (alpha)
History available at github.com/OliverMatthews/rubiksCube/

Oli Matthews 2019
"""
# Imports relevant libraries
import time
import datetime
import solve
import checks as chk

# Class contains developer mode settings which can be toggled on or off
class devFunctions:
    # Initialises the settings and sets the default state for each toggle.
    def __init__(self):
        self.sequencePrinting = False
        self.simFailStatsPrinting = True
        self.simTimeStatusPrinting = True
        self.finalTimeStatsPrinting = True
        self.saveSolutions = True
    
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
    
    # Toggles whether the estimated time remaining should be printed to the
    # console when running simulations. Default state for this is ON.
    def toggleSimTimeStatusPrinting(self, boolean):
        if boolean == True:
            self.simTimeStatusPrinting = True
            print("DEV: Simulation estimated time remaining status printing is now ON! (this is the default state)")
        elif boolean == False:
            self.simTimeStatusPrinting = False
            print("DEV: Simulation estimated time remaining status printing is now OFF!")
    
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

# Useful for running many simulations of randomly shuffling the cube, then
# solving it and testing to ensure that the cube is arranged correctly. Prints
# information to the console after running all simulations indicating success
# or failure statistics.
def runSimulations(numberOfSimulations):
    # Used to count the number of complete simulations.
    simCounter = 0
    
    # Used to count the total number of successes and failures.
    if devSettings.simFailStatsPrinting == True:
        successCounter = 0
        failCounter = 0

    # Used for estimating the time remaining on the simulations.
    if devSettings.simTimeStatusPrinting == True:
        lastPercentageComplete = 0 # Only required if relevant setting enabled.
    startTime = time.time()
    
    # Loop runs until the total number of simulations completed is the same as
    # the number of simulations required.
    while simCounter < numberOfSimulations:
        
        # Randomly shuffles the cube 100 times - enough to guarantee a random
        # shuffle.
        solve.a.randomShuffle(30)
        if devSettings.saveSolutions == True:
            solve.a.sequenceLog = ""
            logCubeState(simCounter + 1)
        
        # Runs the solving functions to complete the cube.
        solve.totalSolve()
        simCounter += 1
        
        # Prints the complete sequence of moves used to solve the cube, if
        # sequence logging is enabled in dev settings.
        if devSettings.saveSolutions == True:
            logSequence()
            
        # Only runs if the simFailStatsPrinting developer setting is enabled.
        if devSettings.simFailStatsPrinting == True:
            
            # If the simulation fails the wholeCube check, adds 1 to the fail
            # counter. Otherwise, adds one to the success counter. 
            if chk.wholeCube(solve.a.side1, solve.a.side2, solve.a.side3, solve.a.side4, solve.a.side5, solve.a.side6) == False:
                failCounter += 1
            else:
                successCounter += 1
        
        # Only runs if the simTimeStatusPrinting developer setting is enabled.
        if devSettings.simTimeStatusPrinting == True:
            # Calculates the percentage completion of all the simulations.
            percentageComplete = (simCounter / numberOfSimulations) * 100
            
            # If the percentage completion (as an integer) has increased, 
            # prints the percentage completion and the estimated time remaining
            # to the console.
            if int(percentageComplete) > int(lastPercentageComplete):
                print(str(int(percentageComplete)) + "% done on " + str(int(numberOfSimulations)) + " simulations.")
                
                # Time data
                splitTime = time.time() - startTime
                timePerPercent = splitTime / percentageComplete
        
                estTimeRemaining = int(timePerPercent * (100 - percentageComplete))
                
                print("Estimated time remaining: " + str(datetime.timedelta(seconds=estTimeRemaining)) + " (HH:MM:SS).")
            
            # Updates the most recent percentage of completion for comparison 
            # use on the next simulation.
            lastPercentageComplete = percentageComplete
    
    # Gets the end time after the simulations have finished running.
    endTime = time.time()
    
    # Blank line before the statistics printouts start.    
    print("")
    
    # Only prints out pass/fail statistics if relevant setting is enabled.
    if devSettings.simFailStatsPrinting == True:
        # Calculates pass/fail rate
        successRate = (successCounter / (successCounter + failCounter)) * 100
        
        # Prints failure information if any of the simulations failed.
        if failCounter > 0:
            print(str(successCounter) + " successful simulations.")
            print(str(failCounter) + " failed simulations.")
            print("Approximately " + str(int(successRate)) + "% of simulations passed.")
            print("")
            
        # If all sims passed all checks, does not print any of the failure info
        # to the console - just prints that all sims were successful.
        else:
            print("All " + str(numberOfSimulations) + " simulations passed.")
        
        # Blank line to separate statistics categories.
        print("")
    
    # Only prints out final time statistics if relevant setting is enabled.
    if devSettings.finalTimeStatsPrinting == True:
        # Time Statistics. Calculates the total time taken to run all simulations,
        # the number of simulations completed each second, and the average time
        # to complete a single simulation.
        timeTaken = endTime - startTime
        simsPerSecond = numberOfSimulations / timeTaken
        avgTimePerSim = timeTaken / numberOfSimulations
        
        print("The total time to run " + str(numberOfSimulations) + " simulations was " + str(datetime.timedelta(seconds=int(timeTaken))) + " (HH:MM:DD)")
        print("An average of around " + str(int(simsPerSecond)) + " simulations were run per second.")
        print("Average time to complete one simulation was " + str(avgTimePerSim) + " seconds.")

def logSequence():
    file = open("sequenceLog.txt", "a")
    file.write("\n" + str(int(len(solve.a.sequenceLog)/2)) + " moves were taken to complete this cube.")
    file.write("\n" + "Solution sequence: " + "\n" + sequenceSpacer(solve.a.sequenceLog) + "\n" + "\n")
    file.close()
    
def logCubeState(simNo):
    file = open("sequenceLog.txt", "a")
    file.write("*** SIMULATION NUMBER " + str(simNo) + " ***")
    file.write("\n" + "Cube starting state: ")
    
    file.write("\n" + "Side 1: ")
    for i in range(solve.a.cubeSize):
        file.write("\n")
        for j in range(solve.a.cubeSize):
            file.write(solve.a.side1[i][j] + " ")
    
    file.write("\n" + "Side 2: ")
    for i in range(solve.a.cubeSize):
        file.write("\n")
        for j in range(solve.a.cubeSize):
            file.write(solve.a.side2[i][j] + " ")
            
    file.write("\n" + "Side 3: ")
    for i in range(solve.a.cubeSize):
        file.write("\n")
        for j in range(solve.a.cubeSize):
            file.write(solve.a.side3[i][j] + " ")
            
    file.write("\n" + "Side 4: ")
    for i in range(solve.a.cubeSize):
        file.write("\n")
        for j in range(solve.a.cubeSize):
            file.write(solve.a.side4[i][j] + " ")
            
    file.write("\n" + "Side 5: ")
    for i in range(solve.a.cubeSize):
        file.write("\n")
        for j in range(solve.a.cubeSize):
            file.write(solve.a.side5[i][j] + " ")
            
    file.write("\n" + "Side 6: ")
    for i in range(solve.a.cubeSize):
        file.write("\n")
        for j in range(solve.a.cubeSize):
            file.write(solve.a.side6[i][j] + " ")
            
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