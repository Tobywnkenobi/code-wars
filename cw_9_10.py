def best_friend(txt, a, b):
    index = 0
    while index < len(txt):
        index = txt.find(a, index)
        if index == -1:  
            break
        if index == len(txt) - 1 or txt[index + 1] != b:  
            return False
        index += 1  
    return True




"""
Sarah's one liner:

def best_friend(txt, a, b):
    return txt.count(a) == txt.count(a+b)

    
"""