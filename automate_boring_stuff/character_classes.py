"""

\d Any numeric digit from 0 to 9
\D Any character that in *not* a numeric digit from 0 to 9
\w Any letter, numeric digit or the underscore character(Think of this as matching "word" characters)
\W Any character that is *not* a letter, numeric digit or the underscore character
\s Any space, tab or newline character(Think of this as matching "space" characters)
\S Any character that in *not* a space, tab or newline

The character class [0-5] will match only the numbers 0 to 5;
this is much shorter than typing (0|1|2|3|4|5)

Note that while \d matches digits and \w matches
digits, letters and the underscore,
there is no shorthand character class that matches only letters
(Though you can use the [a-zA-Z] character class)

import re

xmasRegex = re.compile(r' \d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,
7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

#  The regular expression \d+s\w+ will match text that has one or more
numeric digits(\d+), followed by a whitespace character(\s), followed by
one or more letter/digit/underscore characters(\w+).
The *findall()* method returns all matching strings of the regex pattern in a list.

will return:
['12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,
7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge']


"""
