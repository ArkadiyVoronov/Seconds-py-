import re


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  #  has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
#  will return a list of string matches:
#  '415-555-9999', '212-555-0000'

phoneNumRegexGroups = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  #  has groups
print(phoneNumRegexGroups.findall('Cell: 415-555-9999 Work: 212-555-0000')
#  wil return a list of tuples of strings,
#  (one string for each group):
#  [('415', '555', '9999'), ('212', '555', '0000')]
