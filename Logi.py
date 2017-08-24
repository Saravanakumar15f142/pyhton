class Login:
    import collections
    store=collections.namedtuple("userName" "userType","password")
    def __init__(self,user,userName,userType,password):    
        self.userName=userName
        self.userType=userType
        self.password=password
        self.user=user
        if(self.user=="new"):
            #details=store(self.userName,self.userType,self.password)
            new=(self.userName,self.userType,self.password)
            user=user+new
            print("Register successfully")
            
    def check(user,userName,userType,password):
        else:
            for i in user:
                if(self.userName==user[0] and self.userType==user[1]and self.password==user[2]):
                    print("Login succesfully")
                    return True
                    
            
        
