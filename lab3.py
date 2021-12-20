# Lab 3
# Author: Arianne Ghislaine Rull
# Email: arull@my.yorku.ca
# Student ID: 219129527
# Section A

# Code for task 1 after this line
print("\n--- Task 1 ---: Compute Fare")

userTripInput = (int(input("(1) One way or (2) round trip?\nEnter 1 or 2: ")))
userAgeRangeInput = (int(input("Select Age Range:\n(1) Under 12\n(2) 13-64\n(3) 65 or older\nEnter 1, 2, or 3: ")))

if (userTripInput == 1 and (userAgeRangeInput == 1 or userAgeRangeInput == 3) ):
    print("Total amount due: $0.90 [one way (reduced fare)]")
elif (userTripInput == 1 and userAgeRangeInput == 2):
    print("Total amount due: $1.80 [one way (full fare)]")
elif (userTripInput == 2 and (userAgeRangeInput == 1 or userAgeRangeInput == 3) ):
    print("Total amount due: $1.75 [round trip (reduced fare)]")
elif (userTripInput == 2 and userAgeRangeInput == 2):
    print("Total amount due: $3.50 [round trip (full fare)]")



# Code for task 2 after this line
print("\n--- Task 2 ---: Parse string")
userWordInput = input("Input a string: ")
countWordLength = len(userWordInput)

x = 0
for i in range (1, countWordLength+1):
    if (userWordInput[x]) == " ":
        outputTheSpace = F"str[{x}] = SPACE"
        print(outputTheSpace)
        x = x + 1
        continue
    outputTheChar = F"str[{x}] = {userWordInput[x]}"
    print(outputTheChar)
    x = x + 1

emptyString = ""
while countWordLength > 0:
    emptyString += userWordInput[ countWordLength - 1 ]
    countWordLength = countWordLength - 1
print("Reverse no spaces: ",emptyString.replace(" ", ""))



# Code for task 3 after this line
print("\n--- Task 3 ---: The maximum *even* number")

list = []
counterForPositiveEvenNum = 0
print("Keep entering positive integer\nTo quit, input a negative integer")
while (counterForPositiveEvenNum == 0):
    userPostiveIntInput = int(input("Enter a number: "))

    if (userPostiveIntInput < 0 ): #negative
        counterForPositiveEvenNum = counterForPositiveEvenNum + 1
        if len(list) == 0:
            print("Largest even number: 0")
        else:
            list.sort()
            #print(list)
            outputLargestEvenNum = F"Largest even number: {list[-1]}"
            print(outputLargestEvenNum)

    else:
        countForPositiveEvenNum = 0
        while (countForPositiveEvenNum == 0):
            if (userPostiveIntInput % 2) == 0:
                list.append(userPostiveIntInput)
            countForPositiveEvenNum = countForPositiveEvenNum + 1

# Code for task 4 after this line
print("\n--- Task 4 ---: Better triangle draw")


N = -1
while (N < 5 or N > 20):
    N = int(input("Enter number: "))

for iTriangle in range(N):
    print("-" * iTriangle + "\\")
for iTriangle in range(N, N + 1):
    print("-" * iTriangle + "|")
for iTriangle in range(N - 1, -1, -1):
    print("-" * iTriangle + "/")

input("Press enter to quit.")