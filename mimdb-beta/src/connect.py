"""
    MimDB project.
    Class for work with database connection.
"""

# Imports
import os
from .data_control import DataControl
# End

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

class Connect:

    __user = open(r'config', 'r').readlines()[0].split('\n')[0]
    __password = open(r'config', 'r').readlines()[1]

    def __init__(self):
        self.connection = False
        self.dataControl = DataControl()

    def connect(self, user: str, password: str):
        '''Connect to database.'''
        self.user = str(user)
        self.password = str(password)
        if Connect.__user == self.user and Connect.__password == self.password:
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

    def change_info(self, user: str, password: str):
        '''Change database username and password'''
        if self.is_connect() == True:
            info = "{}\n".format(user) + "{}".format(password)

            configFile = open(r'config', 'w')
            configFile.write(info)
            configFile.close()

            Connect.__user = str(user)
            Connect.__password = str(password)

            self.dataControl.log("Username and Password changed.")

        else:
            return False
        
        return True