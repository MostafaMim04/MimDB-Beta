"""
    MimDB project.
    This class controls saving data in database with writing method.
    As soon, the writing method will change to read-memory method.
"""

# Imports
from .data import database as d
import json
import os
import datetime
# End

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

class DataControl:
    def __init__(self):
        pass

    def changes(self, changes: dict):
        try:
            datajson = json.dumps(changes, sort_keys=True)
            dataFile = open('data.py', 'w')
            dataFile.write("database = " + str(datajson))
            dataFile.close()

            return True

        except Exception as e:
            return e

    def log(self, error):
        errorText = "[{}]: {}\n".format(str(datetime.datetime.now()), str(error))

        errorFile = open(r'log.txt', 'a')
        errorFile.write(errorText)
        errorFile.close()
        