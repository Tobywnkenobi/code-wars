
#     -Figure out wher the input and its type are
#     -Set up a function
#     -Figure out what the output and its type are
#     -Gather your Knowledge
#     -Gathers your contraints (Not Always Necessary)
#     -Determine a Logical way to solve the problem
#      -Write each step out in English
#       -Write each step out in Python-esse (sudo-code)
#       -Invoke and Test your function




"""
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
"""
#make_binary = [45385593107843568]
make_binary = [3,6,6,0,5,8,5,6,2,0,3,0,8,4,9,4,9,0,1,3,4,3,8,8,0,8,5]
return_binary = []


def fake_bin(x: list) -> str:
    for i in x:
        if i >= 5:
            return_binary.append("1")
        else:
            return_binary.append("0")
    return ''.join(return_binary)


# def fake_bin(x: s) -> str:
#     for i in make_binary:                       
#         if int(i) >= 5:                         
#             return_binary.append("1")           
#         else:
#             return_binary.append("0")          
#     return (return_binary)

 
# result = fake_bin(return_binary)
# print(result)