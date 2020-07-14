"""
    MimDB project.
    Class for work with database connection.
"""

class Connect:
    
    user = open(r'C:\Users\Mosttafa\OneDrive\myprojects\MimDB\mim\src\config.txt', 'r').readlines()[0].split('\n')[0]
    password = open(r'C:\Users\Mosttafa\OneDrive\myprojects\MimDB\mim\src\config.txt', 'r').readlines()[1]

    def __init__(self):
        self.connection = False

    def connect(self, user: str, password: str):
        '''Connect to database.'''
        self.user = str(user)
        self.password = str(password)
        if Connect.user == self.user and Connect.password == self.password:
            self.connection = True
            return True
        else:
            self.connection = False
            raise KeyError("The username or password is incorrect.")

    def is_connect(self):
        '''Check is connect to database'''
        if self.connection == False:
            return False
        else:
            return True

    def disconnect(self):
        '''Disconnect from database'''
        self.connection = False
        return True

