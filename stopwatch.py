import time
print("Press ENTER TO BEGIN, press ENTER for a new lap")
input() #press ENTER to begin
print("Started")
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print("Lap number {}, total time: {}, lap time: {}".format(lapNum, totalTime, lapTime))
        lapNum += 1
        lastTime = time.time()



except KeyboardInterrupt:
    print("Good bye")
