"""
Rubix Cube Solver - Developer Functions

v0.6 (alpha)
History available at github.com/OliverMatthews/rubiksCube/

Oli Matthews 2019
"""
# Imports relevant libraries
import time
import datetime
import solve
import checks as chk

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
        solve.a.randomShuffle(100)
        
        # Runs the solving functions to complete the cube.
        solve.totalSolve()
        
        # Checks if the green cross was completed correctly.
        if chk.greenCross(solve.a.side1) == False:
            failCounter += 1
            greenCrossFailCounter += 1
            
        # Checks if the green side was completed correctly.
        elif chk.greenSide(solve.a.side1) == False:
            failCounter += 1
            greenSideFailCounter += 1
            
        # Checks if the centre edges adjacent the green side are aligned
        # correctly.
        elif chk.alignedCenters(solve.a.side2, solve.a.side3, solve.a.side4, solve.a.side5) == False:
            failCounter += 1
            alignedCentersFailCounter += 1
        
        # Checks if the corner pieces adjacent the green side are aligned
        # correctly.
        elif chk.alignedCorners(solve.a.side2, solve.a.side3, solve.a.side4, solve.a.side5) == False:
            failCounter += 1
            alignedCornersFailCounter += 1
        
        # Checks if the first two rows closest the green side on the white,
        # red, yellow and orange sides have been completed correctly.
        elif chk.firstTwoRows(solve.a.side2, solve.a.side3, solve.a.side4, solve.a.side5) == False:
            failCounter += 1
            firstTwoRowsFailCounter += 1
        
        elif chk.blueCross(solve.a.side6) == False:
            failCounter += 1
            blueCrossFailCounter += 1
            
        elif chk.blueSide(solve.a.side6) == False:
            failCounter += 1
            blueSideFailCounter += 1
            
        elif chk.topLayerCorners(solve.a.side2, solve.a.side3, solve.a.side4, solve.a.side5) == False:
            failCounter += 1
            topLayerCornersFailCounter += 1
            
        elif chk.wholeCube(solve.a.side1, solve.a.side2, solve.a.side3, solve.a.side4, solve.a.side5, solve.a.side6) == False:
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
    