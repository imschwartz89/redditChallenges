#DONE

#https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/

#returns a list that has no zeroes in it
def eliminateZero(arr):
    newArr = [i for i in arr if i != 0]
    return newArr

#returns a list that has been sorted in descending order
def sortDesc(arr):
    newArr = sorted(arr, reverse=True)
    return newArr

#returns whether a number is less than or equal to the length of a list
def lengthCheck(num, arr):
    return len(arr) < num

#returns a list that has 1 subtracted from the first num indexes of the list
def frontReduction(num, arr):
    index = num
    newArr = arr
    if index > len(newArr):
        index = len(newArr)
    for i in range(index):
        newArr[i] -= 1
    return newArr

# Havel-Hakimi Alg
#returns whether everyone is telling the truth or someone is lying
def hh(arr):
    newArr = arr
    while True:
        newArr = eliminateZero(newArr)
        if len(newArr) == 0:
            return True
        else:
            newArr = sortDesc(newArr)
            N = newArr.pop(0)
            if lengthCheck(N, newArr): #or N > len(newArr)
                return False
            else:
                newArr = frontReduction(N, newArr)

#main test

# test zero elim function [WORKS]
#arr = [0] #[1, 0, 2, 3, 4, 0, 8]
#arr = eliminateZero(arr)
#print(arr)

# test sortDesc function [WORKS]
#arr = [1, 2, 5, 4, 6, 3, 3]
#arr = sortDesc(arr)
#print(arr)

# test lengthCheck function [WORKS]
#arr = [] #[5, 5, 5, 5, 5]
#print(lengthCheck(2, arr))

#test frontReduction function [WORKS]
#arr = [1] #[5, 4, 3, 2, 1]
#print(frontReduction(0, arr))

#test hh function [WORKS]
print(hh([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]))
print(hh([4, 2, 0, 1, 5, 0]))
print(hh([3, 1, 2, 3, 1, 0]))
print(hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]))
print(hh([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]))
print(hh([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]))
print(hh([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]))
print(hh([2, 2, 0]))
print(hh([3, 2, 1]))
print(hh([1, 1]))
print(hh([1]))
print(hh([]))
