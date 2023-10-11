'''
# How to solve a problem:

#     -Figure out wher the input and its type are
#     -Set up a function
#     -Figure out what the output and its type are
#     -Gather your Knowledge
#     -Gathers your contraints (Not Always Necessary)
#     -Determine a Logical way to solve the problem
#      -Write each step out in English
#       -Write each step out in Python-esse (sudo-code)
#       -Invoke and Test your function



This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

if number divided by 2 has no remainder - (num % 2) == 0: else odd


'''
# def simple_multiplication(number):
#     if number % 2 == 0:
#         return number * 8
#     else:
#         return number * 9
    
    
def simple_multiplication(number):
    if number % 2 == 0:
        new_num = number * 8
        return new_num
    else:
        new_num = number * 9
        return new_num


print(simple_multiplication(6))
print(simple_multiplication(2))
print(simple_multiplication(1))
print(simple_multiplication(8))
print(simple_multiplication(4))
print(simple_multiplication(5))