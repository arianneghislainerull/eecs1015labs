######
# EECS1015 - York University
#
# Topic 9 - MinMaxList class
#
# Lab 9
# Author: Arianne Ghislaine Rull
# Email: arianneghislaine@gmail.com
# Student ID: 219129527
# Section A
####

class MinMaxList:
    def __init__(self, initializeList):
        self.listData = initializeList
        self.listData.sort()

    def insertItem(self, item, printResult = False):
        m = 0
        if len(self.listData) == 0:
            self.listData.append(item)
        elif item >= self.listData[-1]:
            self.listData.append(item)
            m = len(self.listData)
        else:
            #let m be the index of self.listData
            for m in range(len(self.listData)):
                if self.listData[m] < item:
                    m = m + 1
                elif self.listData[m] > item:
                    self.listData.insert(m, item)
                    break
        if printResult == True:
            print(F"Item ({item}) inserted at location {m}\n{self.listData}")

    def getMin(self):
        if len(self.listData) == 0:
            return None
        result = self.listData[0]
        del self.listData[0]
        return result

    def getMax(self):
        if len(self.listData) == 0:
            return None
        result = self.listData[-1]
        del self.listData[-1]
        return result

    def printList(self):
        print(self.listData)


# Main function is given.
def main():
    aList = MinMaxList([10, 11, 99, 1, 34, 88])
    bList = MinMaxList([88, 0])
    print("Starting aList: ", aList.listData)
    print("Starting bList: ", bList.listData)

    min1 = aList.getMin("MIN")
    min2 = bList.getMin("MIN")
    print("MinMaxList minimum with aList is %d" % (min1))
    print("MinMaxList minimum with bList is %d" % (min2))

    aList.insertItem(97)
    bList.insertItem(3)
    print("Insert 97 to aList")
    print("Instert 3 to bList")

    max1 = aList.getMax("MAX")
    max2 = bList.getMax("MAX")
    print("MinMaxList maximum with aList is %d" % (max1))
    print("MinMaxList maximum with bList is %d" % (max2))


if __name__ == "__main__":
    main()