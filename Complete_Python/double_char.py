'''
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
Good Luck!

def double_char(s):
    for s in test:
       s=(len(char * 2))
    print(s)
'''
def double_char(s):
    s = s.lower()
    result = ""
    for char in s:
        result += char *2
        return result
       

print(double_char("String"))
