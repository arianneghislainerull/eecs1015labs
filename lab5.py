#########################
# EECS1015 - Lab 5
# Arianne Ghislaine Rull
# 219129527
# arull@my.yorku.ca or arianneghislaine@gmail.com
# Section A
#########################

from random import randint as rd

def task1():
    listOfNums = []
    def generateRandomList(listSize, maxInt):
        for i in range(1, listSize+1):
            numInTheList = rd(1, maxInt)
            listOfNums.append(numInTheList)
        return listOfNums

    def computeAverage(listOfNums):
        sumOfNumsInTheList = sum(listOfNums)
        average = sumOfNumsInTheList / len(listOfNums)
        fourDecimalsAverage = round(average, 4)
        return fourDecimalsAverage

    def mainTask1():
        listSize = int(input("Input list size: "))
        maxInt = int(input("Input max int: "))
        generateRandomList(listSize, maxInt)
        print(F"Generated list\n{listOfNums}")
        print(F"Average value = {computeAverage(listOfNums):.4f}")

    mainTask1()


def task2():
    wordsListOfString = []
    def stringToCharLst(inputString):
        listOfString = list(inputString)
        return listOfString

    def charsToWord(listOfString):
        dictionary = {'0':'zero', '1':'one', '2': 'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '-':'dash'}
        for i in listOfString:
             for y in dictionary.keys():
                  if i == y:
                       wordsListOfString.append(dictionary.get(y))
        return wordsListOfString


    def sayWordList():
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty("rate", 200)
        nwSeparator = " "
        new = nwSeparator.join(wordsListOfString)
        engine.say(new)
        engine.runAndWait()

    def mainTask2():
        inputString = input("Enter phone number as XXX-XXX-XXXX\nType here: ")
        print(F"{stringToCharLst(inputString)}\n{charsToWord(stringToCharLst(inputString))}")
        separator = "->"
        z = separator.join(charsToWord(stringToCharLst(inputString)))
        print(z)
        yesOrNo = input("Say word list? (Y/N) ")
        if yesOrNo == "y" or yesOrNo == "Y":
             sayWordList()

    mainTask2()

def main():
    print("\n--------- TASK 1: Random List -------------")
    task1()
    print("\n--------- TASK 2: Phone number to text ---")
    task2()

    input("Press enter to exit.")


if __name__ == "__main__":
    main()