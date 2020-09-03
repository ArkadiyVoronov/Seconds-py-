import re

#  matching every character that insn't a vowel
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')

""" will return:
['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.',
' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

By placing a caret character (^) just after opening bracket,
you can make a *negative character class*.
It will match all the characters that are *not* in the character class.
"""
