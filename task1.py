
# Task1
"""
Task: Format and Analyze a Sentence
Description: Given a sentence, perform the following operations:

- Convert the entire sentence to uppercase.
- Count the number of occurrences of the letter 'E'.
- Replace all occurrences of the word "bad" with "good".
- Capitalize the first letter of each word.
- Find the length of the modified sentence.
- Extract a substring from the modified sentence, Get the first 10 characters.

Sample Input:
-------------
sentence = "This is a bad example of a bad situation."

Sample Output:
--------------
Uppercase: THIS IS A BAD EXAMPLE OF A BAD SITUATION.
Occurrences of 'E': 2
Replaced: This is a good example of a good situation.
Capitalized: This Is A Good Example Of A Good Situation.
Length: 43
Sliced Substring: This is a 
"""


task1 = "this is a bad example of a bad situation."



t = task1.upper()
a= task1.count("e")
s= task1.replace("bad", "good") 
task1=s.capitalize()
print(t)
print(a)
print(s)
print(task1)
print(len(task1))
print(task1 [0:10])




