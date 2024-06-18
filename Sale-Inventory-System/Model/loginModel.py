class LoginModel:
    def __init__(self,provided_credentials:list):
        self.provided_credentials = [cred for cred in provided_credentials]
    
    def getLevelOfAccess(self)->str:
        #check if username and password exists and matches data within database if true get levelaccess and return it as a string "Manager/Admin" or Staff, else return false
        username = self.provided_credentials[0]
        password = self.provided_credentials[1]
        print(f"username: {username}, password: {password}")
        if username == "ej" and password == "abcdefg":
            return ["Manager", "010102"] #and return userID// return ["Manger", user ID]
        elif username == "kurt" and password == "123":
            return ["Staff","010103"]
        else:
            return False