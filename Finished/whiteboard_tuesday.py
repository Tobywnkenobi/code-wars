# The Hamming Distance is a measure of similarity between two strings of equal length. Complete the function so that it returns the number of positions where the input strings do not match.

# Examples:
#a = "I like turtles"
#b = "I like turkeys"
# Result: 3

#a = "Hello World"
#b = "Hello World"
# Result: 0

a = "espresso"
b = "Expresso"
# Result: 2

# Notes:
# You can assume that the two inputs are ASCII strings of equal length.

def h_distance(a, b):
    count = 0
    if len(a) != len(b):
        raise ValueError("Strings must be equal length")
    
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count
answer = h_distance(a, b)
print(answer)
