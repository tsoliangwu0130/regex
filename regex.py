import re

pattern = 'abc'
string = 'abcdef'
match = re.search(pattern, string)

print(match.group())
