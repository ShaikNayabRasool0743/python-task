""" 
7. Given two variables a and b, swap their values using a temporary variable 
"""
#n1 = int(input())
#n2 = int(input())
#print("original: ", n1, n2)

#temp = n1
#n1 = n2
#n2 = temp
#print(f"after swapping {n1, n2}")

"""
h/w: print the id() of both variables before and after swapping.
"""
n1=int(input())
n2=int(input())
print(f"before swapping{id(n1),id(n2)}")
n3=n1
n1=n2
n2=n3
print(f"After swapping{id(n1),id(n2)}")