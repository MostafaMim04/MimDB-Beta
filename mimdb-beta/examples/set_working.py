"""
    MimDB project.
    version: 0.0.1
    descreption:
        The first version of mimdb that coded full python.
        This file explained how to work with keys and how to set a value for they.
"""

# Import the mudole
from main import Mim

#First of all, connect to database
m = Mim()
m.connect('root', 'root')   # By defult, username and password is root


# Set a value for a key
m.mset('keyname', 'value')  # Set "value" for "keyname"


# Get a value of a key
m.mget('keyname')   # Get the value of "keyname" and it will return "value"