# Importing re library for regular expressions
import re
# Importing collections library that allows us to count the occurances of words
import collections

text = open('book.txt').read().lower()
words = re.findall('\w+', text)
print (collections.Counter(words).most_common(5))