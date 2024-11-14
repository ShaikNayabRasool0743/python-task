""" 
1. Take two inputs, 
	check if their sum is greater than 100 or if one of them is divisible by 10.
"""
#n1 = int(input())
#n2 = int(input())
#cond1 = (n1+n2)>100
#cond2 = (n1%10==0) or (n2%10==0)
#print(cond1 or cond2)

"""
h/w: Take three inputs, 
	check if their sum is greater than 100 or if one of them is divisible by 10.

"""
n1=int(input("enter a n1 num: "))
n2=int(input("enter a n2 num: "))
n3=int(input("enter a n3 num: "))
cond1=(n1+n2+n3)>100
cond2=(n1%10==0) or(n2%10==0) or (n3%10==0)
print(cond1 or cond2)