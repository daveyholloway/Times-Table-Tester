__author__ = 'D7998'
# Hardcore times table quiz, does all times tables and records how long
# you take to give you an average response time!
#
# MODIFICATION HISTORY
# ====================
# When       Who             Why
# ---------- --------------- ------------------------------------------
# 18/11/2015 Dave Hol'       Initial Version
# 19/11/2015 Dave Hol'       Write the results to a file to track improvements,
#                            also prompt for a name to distinguish who's done
#                            what. File is JSON format.

# Import required libraries
import random
import time
import json

done=False                  # Set to TRUE and we'll stop
score=0                     # Keep track of the score
tries=0                     # keep track of the number of tries
totalTime=0                 # Total time to answer everything
totalTimeCorrect=0          # Total time to answer correctly
totalTimeIncorrect=0        # Total time to answer incorrectly

filePath = "c:\\temp"       # Where we're keeping the results
fileName = "ttResults.txt"  # The results filename

# Get a name to identify the results
name = input("What is your name? : ")

# Keep on going until done
while not done:
    # Count a try
    tries += 1

    # record the time the question was asked
    startTime   =time.time()

    # Pick a table
    table = random.randint(1,12)
    # Pick a multiplier48
    multiplier = random.randint(1,12)

    # Ask the question
    print("Question " + "{0:02d}".format(tries) + " what is " + str(multiplier) + " times " + str(table) + " ?")

    # Get an answer
    answer = input(">>> ")

    # keep asking until the answer is numeric
    while not str.isnumeric(answer):

        # Try again to get an answer
        answer = input(">>> ")

    # How long did it take to answer?
    timeToAnswer=time.time() - startTime
    print("Answered in " + str(round(timeToAnswer,2)) + " seconds.")

    # Tot up the total time
    totalTime += timeToAnswer

    # is the answer correct?
    if int(answer) == int(table * multiplier):
        # Tot up the total time to answer correctly
        totalTimeCorrect +=timeToAnswer

        print("Well done!")
        score +=1
    else:
        # Tot up the total time to answer incorrectly
        totalTimeIncorrect +=timeToAnswer

        print("Oops, not right!")

    # Think of a reason to finish
    # 20 questions?
    if tries >= 20:
        done=True

# Print some summary info
print("Well done "+ name)
print("You had " + str(tries) + " questions.")
print("You got " + str(score) + " correct.")
print("Your average time to answer was " + str(round(totalTime/tries,2)) + " seconds.")
print("Your average time to answer correctly was " + str(round(totalTimeCorrect/score,2)) + " seconds.")
# Score is the percentage correct divided by the average time to answer
print("Your score today is " + str(round((score*100/tries)/(totalTimeCorrect/score),2)))

# Write the data to a results file for later analysis
# Open the file
f = open(filePath + "\\" + fileName,"a")

# Write out the results in JSON format
json.dump([name, tries, score, totalTime, totalTimeCorrect, totalTimeIncorrect,round((score*100/tries)/(totalTimeCorrect/score),2)],f)

# Bung in a new line
f.write("\n")

# Close the file
f.close()
