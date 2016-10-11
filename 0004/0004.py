
import re
from collections import Counter

words = re.findall('r\w+',open('abc.txt').read().lower())
print(Counter(words))

