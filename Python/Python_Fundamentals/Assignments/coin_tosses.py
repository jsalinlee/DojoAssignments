import random
def coinToss(numFlips):
    headsCount = 0
    tailsCount = 0
    for count in range(numFlips):
        toss = round(random.random() + .01)
        if toss == 1:
            result = "heads"
            headsCount += 1
        else:
            result = "tails"
            tailsCount += 1
        print "Attempt #" + str(count + 1) + ": And it's..." + result + "!"
        print "       Got " + str(headsCount) + " heads and " + str(tailsCount) + " tails so far."
coinToss(5000)
