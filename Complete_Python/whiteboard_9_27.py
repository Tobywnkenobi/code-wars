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

''''
# Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. 
# Can you help him to find out, how many cakes he could bake considering his recipes?

# Write a function cakes(), 
# which takes the recipe (object) and the available ingredients (also an object) and 
# returns the maximum number of cakes Pete can bake (integer). 
# For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
# Ingredients that are not present in the objects, can be considered as 0.

# Examples

# # must return 2
# cakes({flour: 500, sugar: 200, eggs: 1}, 
#      {flour: 1200, sugar: 1200, eggs: 5, milk: 200})

# # must return 0
# cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
'''
def cakes(recipe,ingredients): # O(N)
    output = []  # O(1)
    for k in recipe: #O(N)
        try:
            output.append(ingredients[k]//recipe[k]) # O(1)
        except KeyError:
            return 0
    return min(output) # O(N)