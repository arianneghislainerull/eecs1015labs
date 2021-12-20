# Lab 4
# Author: Arianne Ghislaine Rull
# Email: arull@my.yorku.ca
# Student ID: 219129527
# Section A

from random import randint as rd

print("--- Welcome to High-Low ---\nStart with 100 points. Each round a card will be drawn and shown.\nSelect whether you think the 2nd card will be Higher or Lower than the 1st card.\nThen enter the amount you want to bet.\nIf you are right, you win the amount you bet, otherwise you lose.\nTry to make it to 500 points within 10 tries.\n\n-------------------------------------")

userPoints = 100
userRounds = 1
betType = ""

def getCardValue():
    cardValue = int(rd(2, 14))
    return cardValue

def getCardStr(cardValue):

    if cardValue == 1:
        cardValue = "1"
    elif cardValue == 2:
        cardValue = "2"
    elif cardValue == 3:
        cardValue = "3"
    elif cardValue == 4:
        cardValue = "4"
    elif cardValue == 5:
        cardValue = "5"
    elif cardValue == 6:
        cardValue = "6"
    elif cardValue == 7:
        cardValue = "7"
    elif cardValue == 8:
        cardValue = "8"
    elif cardValue == 9:
        cardValue = "9"
    elif cardValue == 10:
        cardValue = "T"
    elif cardValue == 11:
        cardValue = "J"
    elif cardValue == 12:
        cardValue = "Q"
    elif cardValue == 13:
        cardValue = "K"
    elif cardValue == 14:
        cardValue = "A"

    return cardValue

def getHLGuess():

    #betType = " "
    global betType

    while (betType == "L" or betType == "H"):
        betType = " "

    while not(betType == "L" or betType == "H"):
        userGuess = input("High or Low (H/L)?: ")
        betType = userGuess.upper()

        if betType == "H":
            return "HIGH"
        elif betType == "L":
            return "LOW"


def getBetAmount(maximum, bet=-1):

    maximum = userPoints

    while (bet < 1 or bet > maximum):
        bet = int(input("Enter bet: "))
        if not (bet < 1 or bet > maximum):
            return bet



def playerGuessCorrect(card1, card2, betType):

    playerBetType = betType

    if (card1 < card2):

        if (playerBetType == "HIGH"):
            return True
        else:
            return False
    elif (card1 > card2):

        if (playerBetType == "LOW"):
            return True
        else:
            return False
    else:
        return False



for i in range(1, 11):

    print(F"OVERALL POINTS: {userPoints}  ROUND: {userRounds}/10")
    userRounds = userRounds + 1
    #print(i)

    card1 = getCardValue()
    card2 = getCardValue()

    print(F"First card is a [{getCardStr(card1)}]")

    takeUserGuess = getHLGuess()
    #print(takeUserGuess)
    takeUserBet = getBetAmount(userPoints)

    print(F"Second card is a [{getCardStr(card2)}]")

    checkUserResult = playerGuessCorrect(card1, card2, takeUserGuess)
    print(checkUserResult)

    if checkUserResult == True:
        userPoints = int(userPoints) + int(takeUserBet)
        statementTrue = F"Card1 [{getCardStr(card1)}] Card2 [{getCardStr(card2)}] - You bet {takeUserGuess} for {takeUserBet} - You WON"
        print(statementTrue)
    elif checkUserResult == False:
        userPoints = int(userPoints) - int(takeUserBet)
        statementFalse = F"Card1 [{getCardStr(card1)}] Card2 [{getCardStr(card2)}] - You bet {takeUserGuess} for {takeUserBet} - You LOST"
        print(statementFalse)

    print("-------------------------------------")

    if userPoints == 500 or userPoints > 500:
        statementWin = F"YOU MADE IT TO *{userPoints}* POINTS IN {userRounds-1} ROUNDS!"
        print(statementWin)
        break
    elif userPoints <= 0:
        statementLoseZero = F"YOU HAVE *{userPoints}* POINTS AFTER {userRounds-1} ROUNDS!"
        print(statementLoseZero)
        break
    elif userRounds == 11:
        statementLosePoints = F"ONLY *{userPoints}* POINTS IN {userRounds-1} ROUNDS!"
        print(statementLosePoints)
        break

