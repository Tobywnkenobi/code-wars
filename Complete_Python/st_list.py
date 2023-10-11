'''
# Given a string and an list of integers representing indices, capitalize all letters at the given indices.

# For example:

capitalize("abcdef",[1,2,5]) = "aBCdeF"
# capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
# The input will be a lowercase string with no spaces and a list of digits.
'''
#capitalize = ("abcdef", [1,2,5]) #= "aBCdeF"
capitalize = ("abcdef", [1,2,5,100]) #= "aBCdeF"

def caps(s,indices):
    chars = list(s)
    for index in indices:
        if index < len(chars):
            chars[index] = chars[index].upper()
    return ''.join(chars)

answer = caps(*capitalize)
print(answer)
