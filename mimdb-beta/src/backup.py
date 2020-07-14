"""
    MimDB project.
    Class for getting back up.
"""

# Imports
import json
from .data import database as d
from .data_control import DataControl
# End

class BackUp:
    def __init__(self):
        self.dataControl = DataControl()

    def get_backup(self, address: str):
        '''Get a backup from your database'''
        try:
            dataJson = json.dumps(d, sort_keys=True)
            
            makeBackup = open(r'{}\backup.json'.format(address), 'w')
            makeBackup.write(dataJson)
            makeBackup.close()
            return address

        except Exception as e:
            self.dataControl.log(str(e))
            return e