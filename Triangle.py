# Name: Alice Liang
# EID: axl84
# Unique Section Number: 84825
# Assignment: #10
# Date: 7/15/20

import time
import sys
# Input: grid a 2-D list of integers
# Output: returns a single integer that is the greatest path sum
#         using exhaustive search


def exhaustive_search(grid):

    length = len(grid)
    list = []

    for i in range(length):
        indexList = []
        if i == 0:
            indexList.append(0)
            list.append(indexList)

        else:
            for j in range(len(list)):
                jList = list[j]
                copyList = []
                for k in range(len(jList)):
                    copyList.append(jList[k])

                index = jList[len(indexList) - 1]
                jList.append(index)
                copyList.append(index + 1)
                list.append(copyList)

    largestSum = -sys.maxsize - 1
    for i in range(len(list)):
        sum = 0
        for j in range(len(list[i])):
            index = list[i][j]
            value = grid[j][index]
            sum += value
        if sum > largestSum:
            largestSum = sum

    return largestSum

# Input: grid a 2-D list of integers
# Output: returns a single integer that is the greatest path sum
#         using the greedy approach


def greedy(grid):

    length = len(grid)
    greatestNum = grid[0][0]
    j = 0
    for i in range(1, length):
        if grid[i][j] < grid[i][j+1]:
            j += 1
        greatestNum += grid[i][j]

    return greatestNum

# Input: grid a 2-D list of integers
# Output: returns a single integer that is the greatest path sum
#         using divide and conquer (recursive) approach


def rec_search(grid):

    length = len(grid)
    if length == 1:
        return grid[0][0]

    grid1 = []
    grid2 = []
    for i in range(1, length):
        newGrid1 = []
        newGrid2 = []
        for j in range(i):
            newGrid1.append(grid[i][j])
            newGrid2.append(grid[i][j + 1])
        grid1.append(newGrid1)
        grid2.append(newGrid2)

    sum1 = rec_search(grid1)
    sum2 = rec_search(grid2)
    if sum1 >= sum2:
        return sum1 + grid[0][0]
    else:
        return sum2 + grid[0][0]

# Input: grid a 2-D list of integers
# Output: returns a single integer that is the greatest path sum
#         using dynamic programming


def dynamic_prog(grid):

    length = len(grid)
    greatestNum = []
    for i in range(length-1, -1, -1):
        greatestNumRow = []
        for j in range(i + 1):

            if i == length-1:
                greatestNumRow.append(grid[i][j])
            else:
                if greatestNum[length - i - 2][j] > greatestNum[length - i - 2][j + 1]:
                    greatestNumRow.append(
                        grid[i][j] + greatestNum[length - i - 2][j])
                else:
                    greatestNumRow.append(
                        grid[i][j] + greatestNum[length - i - 2][j + 1])

        greatestNum.append(greatestNumRow)

    return greatestNum[length - 1][0]


def main():

    # read triangular grid from file
    infile = open("triangle.in", "r")
    inpt = infile.read().split('\n')
    grid = []
    for i in range(len(inpt)):
        inpt[i] = inpt[i].split()
        temp = []
        for num in inpt[i]:
            temp.append(int(num))
        grid.append(temp)

    ti = time.time()
    # output greates path from exhaustive search
    exhaustive = exhaustive_search(grid)
    print("The greatest path sum through exhaustive search is", exhaustive)

    tf = time.time()
    del_t = tf - ti
    # print time taken using exhaustive search
    print("The time taken for exhaustive search is", del_t,  "seconds.")

    ti = time.time()
    # output greates path from greedy approach
    greed = greedy(grid)
    print("The greatest path sum through exhaustive search is", greed)

    tf = time.time()
    del_t = tf - ti
    # print time taken using greedy approach
    print("The time taken for greedy search is", del_t,  "seconds.")

    ti = time.time()
    # output greates path from divide-and-conquer approach
    divide = rec_search(grid)
    print("The greatest path sum through divide-and-conquer search is", divide)

    tf = time.time()
    del_t = tf - ti
    # print time taken using divide-and-conquer approach
    print("The time taken for divide-and-conquer search is", del_t,  "seconds.")

    ti = time.time()
    # output greates path from dynamic programming
    dynamic = dynamic_prog(grid)
    print("The greatest path sum through dynamic programming is", dynamic)

    tf = time.time()
    del_t = tf - ti
    # print time taken using dynamic programming
    print("The time taken for dynamic programming is", del_t,  "seconds.")


if __name__ == "__main__":
    main()
