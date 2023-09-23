''''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

To determine if a given string is a pangram, we need to check if each letter of the alphabet is present in the string.

Here's a method to achieve this:

    Convert the input string to lowercase.
    Remove any non-alphabetic characters.
    Convert the string to a set (to remove duplicates).
    Check if this set is equal to the set of all lowercase letters.
'''

def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    s = set(s.lower())
    return alphabet <= s 
