class Model:
    def __init__(self):
        pass

    def levelOfAccess(self,username,password)->str:
        #check if username and password exists and matches data within database if true get levelaccess and return it as a string "Manager/Admin" or Staff, else return false
        return "Manager"