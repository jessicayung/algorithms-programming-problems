"""
Problem 1: Match exact string

Match 'hackerrank'

Regex_Pattern = r'hackerrank'

"""

# Implement
import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))


"""
Problem 2: Matching anything but newline

The dot (.) matches anything (except for a newline).

Match xxx.xxx.xxx.xxx, where x is any character. 

Regex_Pattern = r"...\....\....\...."	# Do not delete 'r'.

"""


"""
Problem 3: Matching Digits and Non-Digit Characters

\d matches any digit [0-9]

\D matches any character that is not a digit

You have a test string S. Your task is to match the pattern xxXxxXxxxx. 
Here x denotes a digit character, and X denotes a non-digit character.

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"

"""

# Implement
print(str(bool(re.search(Regex_Pattern, input()))).lower())

"""
Problem 4: Matching Whitespace & Non-Whitespace Characters

\s matches any whitespace character [ \r\n\t\f ].

\S matches any non-white space character.

You have a test string . Your task is to match the pattern XXxXXxXX. 
Here, x denotes whitespace characters, and X denotes non-white space 
characters.


"""

"""
Problem 5: Matching Word & Non-Word Character

\w matches any word character. 
- Word characters include alphanumeric characters (-, - and -) and 
underscores (_).

\W matches any non-word character.

Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"

Example input: www.hackerrank.com
"""

"""
Problem 6: Start and End

"""
