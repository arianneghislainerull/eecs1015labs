# Lab 1
# Author: Arianne Ghislaine Rull
# Email: arull@my.yorku.ca
# Student ID: 219129527
# Section A

print("\n----Task 1---- BMI Calculator")
## Write Task1 code here
name = input("Enter the name: ")
weight = float(input("Enter the weight in kg: "))
heightCentimetres = float(input("Enter the height in cm: "))

#process name
name = name.lower().title()
print(name)
#process height
heightMetres = heightCentimetres / 100
#process bmi
bmi = weight / (heightMetres) ** 2

print("#################")
outputBMI = f"Name: {name} \nHeight: {heightMetres:.2f} m\nWeight: {weight} kg\nBMI: {bmi:.2f}"
print(outputBMI)

print("\n----Task 2---- Leetspeak Converter")
## Write Task2 code here
longString = input("Enter the long string: ")

longString = longString.upper().strip()
longString = longString.replace("T","+")
longString = longString.replace("A", "@")
longString = longString.replace("E", "3")
longString = longString.replace("I","|")
longString = longString.replace("B","8")
longString = longString.replace("O", "0")
longString = longString.replace("C","[")
longString = longString.replace("S","5")

print(longString)

print("\n----Task 3---- Flipping String")
## Write Task3 code here

stringToBeFlipped = input("Input a long string: ")
stringLength = len(stringToBeFlipped)

stringMiddleDivide = (int(len(stringToBeFlipped) / 2)) # result of / operator is always a float so we had to convert it to an int
#print(stringMiddleDivide)
stringMiddleCharacter = stringToBeFlipped[stringMiddleDivide]
#print(stringMiddleCharacter)

characterOutput = f"This string is {stringLength} characters long. \n The middle character is '{stringMiddleCharacter}'"
print(characterOutput)
uppercaseString = stringToBeFlipped.upper()

spliceBeginningOfString = uppercaseString[0:stringMiddleDivide]
spliceEndOfString = uppercaseString[stringMiddleDivide:stringLength+1]
print("FLIPPED STRING")
print(spliceEndOfString + "|" + spliceBeginningOfString)
#print(uppercaseString[stringMiddleDivide:stringLength+1])
#print(uppercaseString[0:stringMiddleDivide])



print("\n----Task 4---- Multiple numbers")
## Write Task4 code here

userinputMultiplyString = input("Enter numbers to multiply: ")
newStringNumbers = userinputMultiplyString.strip().replace("*", "  ")
print(newStringNumbers)

multiplyStringLength = len(newStringNumbers)
spaceIndex = int(newStringNumbers.find(" "))
num1 = int(newStringNumbers[0:spaceIndex])
num2 = int(newStringNumbers[spaceIndex:multiplyStringLength+1])

product = num1*num2
productStatement = f"{num1} * {num2} = {product}"
print(productStatement)

input("Press enter to exit. ")  # input statement to pause code when finished