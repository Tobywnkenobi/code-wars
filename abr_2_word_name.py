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

"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F

def Cap_letters
    Full_name = (first, last)
    first = first_name
    last = last_name
    print(first.index[0], last.index[0])

    
"""
def abbrevName(name: str) -> str:
    names = name.split()
    
    if len(names) == 1:
        return names[0][0].upper() + "."
    
    first_name, last_name = names
    return first_name[0].upper() + "." + last_name[0].upper()

test_name = "PFavuzzi"
abbrevName(test_name)


