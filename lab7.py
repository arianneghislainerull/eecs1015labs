#########################
# EECS1015 - York University
# Author: Arianne Ghislaine Rull
# Email: arianneghislaine@gmail.com
# Student ID: 219129527
# Lab #7
#########################

import pytest
from typing import List

# Accepts a list of integers
def initializeMinMaxList(myList: List[int]) -> None:   # given
    myList.sort()

def insertItem(myList: List[int], item: int) -> None:  # given
    myList.append(item)
    myList.sort()

def getMinMax(myList: List[int], minormax: str) -> int:   # given -- but requires additional assert
    assert minormax.upper()=="MAX" or minormax.upper()=="MIN", "2nd argument must be 'Min' or 'Max' "
    assert len(myList) != 0 and len(myList) > 0, "list must NOT be empty"
    result: int

    if minormax == "MAX":
        result = myList[-1]
        del myList[-1]
    else:
        result = myList[0]
        del myList[0]
    return result

# Main function is given.
def main():
    aList = [10, 11, 99, 1, 55, 100, 34, 88]
    #aList = []
    print("Starting List: ", aList)
    initializeMinMaxList(aList)
    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("Insert %d %d %d %d" % (min1 - 1, min2 - 1, max1 + 1, max2 + 1))
    insertItem(aList, min1 - 1)
    insertItem(aList, min2 - 1)
    insertItem(aList, max1 + 1)
    insertItem(aList, max2 + 1)

    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("DONE.  Type Enter to exit.")
    input()


if __name__ == "__main__":
    main()

#####
# WRITE YOUR TEST CASES BELOW HERE
#
######

def test_getMinMaxCase1():
    firstList = [3, 4]

    initializeMinMaxList(firstList)
    min = getMinMax(firstList, "MIN")
    # assert statement "Min should be x"
    assert min == 3, "Min should be 3"

    max = getMinMax(firstList, "MAX")
    # assert statement "Max should be y"
    assert max == 4, "Max should be 4"

def test_getMinMaxCase2():
    secondList = [8]
    initializeMinMaxList(secondList)
    min = getMinMax(secondList, "MIN")
    assert min == 8, "Min should be 8"
    insertItem(secondList, min)
    max = getMinMax(secondList, "MAX")
    assert max == 8, "Max should be 8"

def test_getMinMaxCase3():
    thirdList = []
    initializeMinMaxList(thirdList)
    insertItem(thirdList, 2)
    insertItem(thirdList, 8)
    min = getMinMax(thirdList, "MIN")
    assert min == 2, "Min should be 2"
    max = getMinMax(thirdList, "MAX")
    assert max == 8, "Max should be 8"

def test_getMinMaxRequestError():
    fourthList = [6,7,8]
    initializeMinMaxList(fourthList)
    with pytest.raises(AssertionError) as e:
         getMinMax(fourthList,"MID")
    assert e.typename=="AssertionError", "Should raise AssertionError!"

def test_getMinMaxEmptyError():
    fifthList = []
    initializeMinMaxList(fifthList)
    with pytest.raises(AssertionError) as g:
        getMinMax(fifthList, "MIN")
    assert g.typename=="AssertionError", "Should raise AssertionError!"






