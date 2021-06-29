# Name: Alice Liang
# EID: axl84
# Unique Section Number: 84825
# Assignment: #7
# Date: 7/5/20

import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series


def sum_series(v, k):

    sum = 0
    for i in range(v):
        numLines = v // (k ** i)
        if numLines == 0:
            return sum
        else:
            sum += numLines
    return sum

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search


def linear_search(n, k):

    for v in range(n, 0, -1):
        s = sum_series(v, k)
        if n == s:
            return v
        elif s < n:
            return v + 1
    return -1

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search


def binary_search(n, k):

    low = 1
    high = n

    while high >= low:
        v = (high + low) // 2
        s = sum_series(v, k)
        if v == low:
            return high
        if n > s:
            low = v
        elif n < s:
            high = v
        elif s == n:
            return v
    return -1

# Input: no input
# Output: a string denoting all test cases have passed
# def test_cases():
#   # write your own test cases

#   return "all test cases passed"


def main():
    in_file = open("work.in.txt", "r")
    num_cases = int((in_file.readline()).strip())

    for i in range(num_cases):
        inp = (in_file.readline()).split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()


#  if __name__ == "__main__":
main()
