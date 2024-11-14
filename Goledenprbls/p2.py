"""
2. Take two inputs
	check if both of the numbers are even, both are odd, 
    one is even and other is odd.
"""
#n1 = int(input())
#n2 = int(input())

#if n1 % 2 == 0 and n2 % 2 == 0:
 #   print("Both are even")
#elif (n1 % 2 != 0) and (n2 % 2 != 0):
 #   print("Both are odd")
#else:
 #   print("One is even and other is odd")
    


""" 
h/w: Take two inputs, check if both of the numbers 
    are even and divided by 5, 
    both are odd and divided by 5, 
    or one of each divided by 5.
"""
n1=int(input("enter a n1 value: "))
n2=int(input("enter a value: "))

if n1%5==0 and n2%5==0 :
    print("both are even and divided by 5")
elif n1%5!=0 and n2%5!=0:
    print("both are odd and div by 5")
else:
    print("one of each div by 5")
