# Find the numbers starting with 212.

import re

str = '''Ancient Script 21299: The Takenouchi documents are the ancient historical records that have been secretly preserved and passed down from generation to generation by the Takenouchi family, the head of family being the chief priest of the Koso Kotai Jingu shrine. 212-111-5932 '''

regex = r'212\S+'
data=re.findall(regex, str)


print(data)
