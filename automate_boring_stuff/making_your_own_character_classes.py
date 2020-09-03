import re


vowelRexex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
"""  will return:
any vowel, both lowercase and uppercase
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
"""

"""
[a-zA-Z0-9] will match all lowercase, uppercase letters and numbers
[0-5.] will match digits 0 to 5 and a period
"""
