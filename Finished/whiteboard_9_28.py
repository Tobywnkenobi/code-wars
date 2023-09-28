# How to solve a problem:

#     -Figure out wher the input and its type are
#     -Set up a function
#     -Figure out what the output and its type are
#     -Gather your Knowledge
#     -Gathers your constraints (Not Always Necessary)
#     -Determine a Logical way to solve the problem
#      -Write each step out in English
#       -Write each step out in Python-esse (sudo-code)
#       -Invoke and Test your function
'''
# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
# constraints: 
# cannot use .count()
'''
def find_odd(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

example1 = [7]
example2 = [0, 1, 0, 1, 0]
example3 = [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]

result1 = find_odd(example1)
result2 = find_odd(example2)
result3 = find_odd(example3)
print(result1, result2, result3)
