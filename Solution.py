from Login import Login
class Solution:
    newUserId=1110
    print("1.LOGIN \n 2.SIGNUP")
    opt=int(input("enter the option"))
    if(opt==1):
        user="old"
        userName=input("enter the username")
        userType=input("enter the usertype:(Admin/Student)")
        password=input("enter the password")
        oldUser=Login(user,userName,userType,password)
    else:
        user="new"
        userName=newUserId+1
        userType=input("enter the usertype(STUDENT/ADMIN):")
        password=input("set the password")
        newUser=Login(user,userName,userType,password)
        
