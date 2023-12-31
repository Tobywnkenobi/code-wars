'''
Take debugging to a whole new level:

Given a string, remove every single bug.

This means you must remove all instances of the word 'bug' from within a given string, unless the word is plural ('bugs').

For example, given 'obugobugobuoobugsoo', you should return 'ooobuoobugsoo'.

Another example: given 'obbugugo', you should return 'obugo'.

Note that all characters will be lowercase.

Happy squishing!
'''
#bugs = ('obugobugobuoobugsoo'),
# bugs = ('obbugugo'),
# bugs = ('bugs bunny'),
# bugs = ('bugs buggy')

# # 
def debug(s):
    s = s.replace('bugs', 'PLACEHOLDER') 
    s = s.replace('bug', '')
    s = s.replace('PLACEHOLDER', 'bugs')
    return s