"""
    MimDB project.
    Class for working with sets.
"""

# Imports
from .data import database as d
# End

class Sets:
    def __init__(self):
        pass

    def mset(self, key: str, value: str):
        '''Set value of a key.'''
        try:
            d[key] = value
            return value
        except Exception as e:
            return e

    def mget(self, key: str):
        '''Get value of a key.'''
        try:
            return d.get(key, None)
        except Exception as e:
            return e
