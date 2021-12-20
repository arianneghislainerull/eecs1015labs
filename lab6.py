#######################
# Lab 6 - Starting code
# Name: Arianne Ghislaine Rull
# Student ID: 219129527
# email: arianneghislaine@gmail.com / arull@my.yorku.ca
# Section A
#######################

# variables for task 1
dictMenu = {'Fruits': {'Apple': 1.99, 'Banana': 0.59, 'Kiwi': 1.1, 'Grapes': 2.99, 'Pear': 2.15},
            'Drinks': {'Water': 1.0, 'Juice': 3.5, 'Coffee': 1.5, 'Soda': 1.5, 'Tea': 1.25},
            'Dessert': {'Ice Cream': 2.99, 'Pie': 2.5, 'Cake': 2.75},
            'Main Dishes': {'Masala Dosa': 4.25, 'Jianbing': 2.88, 'Falafel': 5.15, 'Pizza': 8.5}}

# variables for task 2
decoder = {80: 'P', 121: 'y', 116: 't', 104: 'h', 111: 'o', 110: 'n', 105: 'i', 115: 's', 99: 'c', 108: 'l', 46: '.',
           32: ' ', 44: ',', 45: '-', 95: '_', 40: '(', 42: '*', 41: ')', 47: '/', 92: '\\', 61: '=', 39: "'", 124: '|',
           96: '`', 58: ':', 59: ';'}
msg1 = [[80, 121, 116, 104, 111, 110], [105, 115], [99, 111, 111, 108, 46]]
msg2 = [[32, 32, 32, 44, 45, 46], [32, 95, 40, 42, 95, 42, 41, 95], [40, 95, 32, 32, 111, 32, 32, 95, 41],
        [32, 32, 47, 32, 111, 32, 92], [32, 40, 95, 47, 32, 92, 95, 41, 32]]
msg3 = [[32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 40], [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 41],
        [32, 32, 32, 32, 32, 95, 95, 46, 46, 45, 45, 45, 46, 46, 95, 95],
        [32, 44, 45, 61, 39, 32, 32, 47, 32, 32, 124, 32, 32, 92, 32, 32, 96, 61, 45, 46],
        [58, 45, 45, 46, 46, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 46, 46, 45, 45, 59],
        [32, 92, 46, 44, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 44, 46, 47]]
msg1Decoded = []
msg2Decoded = []
msg3Decoded = []

def task1():
    for dictionaryId, dictionaryInfo in dictMenu.items():
        print(F"----{dictionaryId}----")
        for key in dictionaryInfo:
            print(F"${dictionaryInfo[key]:.2f}  {key}")

def task2():
    print("--- Message 1 ----")
    for rows in msg1:
        for item in rows:
            for decoderKey, decoderValue in decoder.items():
                if decoderKey == item:
                    msg1Decoded.append(decoderValue)
        msg1Decoded.append(" ")

    separator = ""
    msg1List = [(separator.join(msg1Decoded))]
    msg1FinalList = ' '.join(msg1List).split()

    for words in msg1FinalList:
        print(F"{words}")


    print("--- Message 2 ----")
    for rows in msg2:
        for item in rows:
            for decoderKey, decoderValue in decoder.items():
                if decoderKey == item:
                    msg2Decoded.append(decoderValue)
        msg2Decoded.append("#")

    msg2Phrase = ''.join(msg2Decoded)
    msg2List = msg2Phrase.split("#")

    for rowInList in msg2List:
        print(rowInList)


    print("--- Message 3 ----")
    for rows in msg3:
        for item in rows:
            for decoderKey, decoderValue in decoder.items():
                if decoderKey == item:
                    msg3Decoded.append(decoderValue)

        msg3Decoded.append("#")

    msg3Phrase = ''.join(msg3Decoded)
    msg3List = msg3Phrase.split("#")

    for rowInList in msg3List:
        print(rowInList)

def main():
    print("------ Task 1 ------")
    task1()

    print("------ Task 2 ------")
    task2()

    input('Press enter to finish.')

if __name__ == '__main__':
    main()