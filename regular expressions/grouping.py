import re

pattern = r"((\w+)-\2)"
string = "test-test chow-chow"
duplicates = re.findall(pattern, string)
print(duplicates)

pattern = r'((abc)*(text|test)*)'
string = 'abcabctesttext'
print(re.match(pattern, string).groups())
