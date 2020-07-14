"""
    MimDB project.
    version: 0.0.1
    descreption:
        The first version of mimdb that coded full python.
        This file explained how to get a backup from your database and changing your user and pass.
"""

# Import the mudole
from main import Mim

#First of all, connect to database
m = Mim()
m.connect('root', 'root')   # By defult, username and password is root


# Get backup
m.get_backup('/root/my_data/')  # You must replace your address with /root/my_data/


# Change the user and password of database
m.change_info('test', 'test')   # Replae your user and pass