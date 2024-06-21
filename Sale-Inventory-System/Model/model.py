class Model:
    def __init__(self):
        pass

    def getLevelOfAccess(self,credentials:list)->str:
        #check if username and password exists and matches data within database if true get levelaccess and return it as a string "Manager/Admin" or Staff, else return false
        username = credentials[0]
        password = credentials[1]
        print(f"username: {username}, password: {password}")
        return "Manager"
    
    def registerUser(self,data:list):
        print(data)
        pass