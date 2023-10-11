''''
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
'''
# You can solve this problem using a stack data structure. The idea is to iterate through the characters in the input string and use a stack to keep track of the opening braces. When you encounter a closing brace, you check if it matches the most recent opening brace in the stack. If it does, you pop the opening brace from the stack; otherwise, the string is invalid.

def valid_braces(string):
    stack = []

    brace_map = {')':'(',']':'[','}':'{'}

    for c in string:
        if c in brace_map.values():
            stack.append(c)
        elif c in brace_map.keys():
            if not stack:
                return False
            if stack[-1] == brace_map[c]:
                stack.pop()
            else:
                return False
            
    return len(stack) == 0