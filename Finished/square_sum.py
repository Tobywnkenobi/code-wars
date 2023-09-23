import math

"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 

def square_sum(numbers):
    #your code here

list - len list.  each number *itself, then added together.

"""
# def sum():
#     a = 1**2
#     b = 2**2
#     c = 2**2
#     total = a + b + c
#     return total
# total = sum()

# print (total)


numbers = [1, 2, 2]

def square_sum(numbers):
    add_num = []
    for n in numbers:
        square = n**2
        add_num.append(square)
    return (sum(add_num))

answer = square_sum([4,4,6])

print(answer)







