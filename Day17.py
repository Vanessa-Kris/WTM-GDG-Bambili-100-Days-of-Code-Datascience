s = "foo123bar"
# print("123" in s)

# print(s.find("123"))
# print(s.index("123"))

import re
# print(re.search("123", s))

# if re.search('123', s):
#     print('Found a match.')
# else:
#     print('No match.')

# print(s[3:7])

# print(re.search('[0-9][0-9][0-9]', s))
print(re.search('1.3', s))