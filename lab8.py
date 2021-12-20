# EECS1015 - Lab 8
# Arianne Ghislaine Rull
# 219129527
# arull@my.yorku.ca or arianneghislaine@gmail.com
# Section A

import time
from random import randint as rd

class Snail:
    animationSequence = ["__~@", "_~_@", "~__@"]
    name: str
    speed: float
    frame: int
    pos: float

    def __init__(self, name) -> None :
        self.name = name.upper()
        assert len(name) == 2, "Snail's initials must be 2 characters."
        self.speed = (rd(1,10))/10
        self.frame = 0
        self.pos = 0.00

    def move(self):
        self.pos = self.pos + self.speed
        self.frame = self.frame + 1

        if 2 < self.frame:
            self.frame = 0

    def getIntPos(self) -> int:
        return int(self.pos)         #this becomes an int

    def getName(self) -> str:
        return self.name

    def getStr(self):
        #This method will create a long string that depicts the snail moving.
        longString = ""
        for i in range (0, 46):
            longString = longString + " "
        getPos = Snail.getIntPos(self)
        frameList = Snail.animationSequence[self.frame]

        posSpacesBegin = longString[:getPos]
        posSpacesEnd = longString[getPos:-7]

        return (F"{posSpacesBegin}{frameList}{posSpacesEnd}{self.name}")

def getSnailList():
   snailList = []
   N = int(input("How many snails are racing? "))

   for j in range(0, N):
      snailName = str(input(F"Snail {j+1} two initials: "))
      snail = Snail(snailName)
      snailList.append(snail)

   return snailList

def runRace(snailList) -> None:
    currentTime: int = 1
    dash = "-"
    winner = []
    #print(F"{40*dash}Time {currentTime}")

    while currentTime > 0:
        print(F"{40*dash}Time {currentTime}")
        currentTime = currentTime + 1

        for k in range(len(snailList)):
            getRaceString = snailList[k].getStr()
            print(getRaceString)
            snailList[k].move()
            snailPos = snailList[k].getIntPos()

            if 39 < snailPos:
                winner.append(snailList[k].getName())
                currentTime = 0

        time.sleep(0.2) # 0.2s delay

    print(F"Snail {winner[0]} WON!")

def main():

    count = 0
    while count == 0:
        print("Snail Race...")
        var = getSnailList()
        input("Press enter to start the race.")
        runRace(var)
        userPlayAgain = str(input("Play again (Y)?"))
        if userPlayAgain.upper() != "Y":
            count = count + 1

if __name__ == "__main__":
    main()