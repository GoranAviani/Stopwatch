import time

def main():
    print("Press ENTER TO BEGIN, press ENTER for a new lap")
    input() #press ENTER to begin
    print("Started")
    startTime = time.time()
    lastTime = startTime
    lapNum = 1
    while True:
        userInput = input()  # press ENTER to do a new lap
        if userInput.upper() == "X":
            print("Good bye !")
            break
        else:
            lapTime = round(time.time() - lastTime, 2)
            totalTime = round(time.time() - startTime, 2)
            print("Lap number {}, total time: {}, lap time: {}".format(lapNum, totalTime, lapTime))
            lapNum += 1
            lastTime = time.time()



if __name__ == "__main__":
    main()