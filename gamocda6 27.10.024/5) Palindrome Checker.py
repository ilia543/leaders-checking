# 5) Palindrome Checker (3 ქულა)
# Create a program that checks if a given string is a palindrome (reads the same forward and backward). The function should ignore spaces, punctuation, and capitalization.
# Examples:
# "A man a plan a canal Panama" --> True
# "Hello" --> False

str1 = "A man a plan a canal Panama"

str1 = str1.upper()
str1 = str1.split()
str2 = "".join(str1)
if str2 == str2[::-1]:
    print(True)
else:
    print(False)