
#task2
""" 

TASK: Get the username from the user and generate the userid
For Memory Issues, Limit the userid to length 10 with following conditions
  - if the length of userid is less than 10, then cover it with 0 at prefix
  - if length of userid exceeds 10, then remove the extra characters

For the security reasons, we had to mask the user id with following:
  replace the last two characters with 'X'
Print the userid along with masked userid

Sample Input1:
  nick
Sample Output1:
  000000nick ---- 000000niXX

Sample Input2:
  codewala
Sample Output2:
  00codewala ---- 00codewaXX

Sample Input3:
  SteeveRogers
Sample Output3:
  SteeveRoge ---- SteeveRoXX

"""




#print(userid)



#S = len(userid)
#K = 10-S
#userid = user[:-2:] +K*"" 
#print(userid>10)














#print(userid.rstrip('{G}'))
user = input("Entername:")
userid =  user
T = len(user)
A = T-10

userid = A*"0"+user 
S = user[:-2:] +"XX"
print(S)







#userid = A*"0"+user[:-2:] +"XX"
#print(userid)
#S = userid[ : : :], "XX")
#print(S)



#k= len(userid)
#G = k-10




#M = k-10
#userid =userid.replace("{M}"," ")
#print(userid)
#t =userid.replace("<opr>", "")
#print(t)