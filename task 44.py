"""
Count Even and Odd Numbers in a List

Problem: Write a function that takes a list of numbers and 
		returns a tuple with two values: 
				count of evens and the count of odds in the list.

Hint: Use a loop and conditional statements to determine if a number is even or odd.

SOLVE THIS PROBLEM WITH & WITHOUT ===> filter <====

SAMPLE INPUT: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
SAMPLE OUTPUT: (5, 5)
"""
def Count_Even_and_Odd_Number(numbers):
    even=len(tuple(filter(lambda x: x %2==0,numbers)))
    odd=len(tuple(filter(lambda x:x%2!=0,numbers)))
    return(even,odd)
numbers=[1,2,3,4,5,6,7,8,9,10]
print(Count_Even_and_Odd_Number(numbers))