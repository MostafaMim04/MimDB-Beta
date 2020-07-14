"""
    MimDB project.
    Class for working with lists.
"""

# Imports
from .data import database as d
from .data_control import DataControl
# End

class Lists:
    dataControl = DataControl()
    def __init__(self):
        pass

    def madd(self, key: str, values: list, column: int=0):
        '''
            Add values to a key.

            value must be a str list
        '''
        try:
            for i in values:
                d[key][column].append(i)
            Lists.dataControl.changes(d)

            return True

        except KeyError as e:
            try:
                if str(e) == '\'' + key +'\'':
                    d[key] = [[]]
                    for value in values:
                        d[key][0].append(value)

                    Lists.dataControl.changes(d)

                    return True

            except IndexError:
                return False

        except Exception as e:
            if str(e) == 'list index out of range':
                print(e)
                return False

            else:
                return e

    def madd_column(self, key: str, count_columns: int):

        try:
            for i in range(count_columns):
                d[key].append([])

            Lists.dataControl.changes(d)

            return len(d[key])

        except KeyError as e:
            if str(e) == '\'' + key +'\'':
                d[key] = []
                for i in range(count_columns):
                    d[key].append([])
                
                Lists.dataControl.changes(d)
                
                return len(d[key])

            
        except Exception as e:
            return e

    def mmembers(self, key: str, column: int=0):
        '''Get members of a list'''
        try:
            return d.get(key, None)[column] if d.get(key, None) != None else None

        except Exception as e:
            return e

    def mrem(self, key: str, values: list):
        '''Remove one or some values from a key'''
        try:
            removable = None
            count = 0
            number = 0
            for column in d[key]:
                for value in column:
                    if value in values:
                        removable = value
                        count += 1
                
                for i in range(int(count)):
                    d[key][number].remove(removable)

                number += 1
            
            Lists.dataControl.changes(d)

            return True

        except KeyError as e:
            return False

        except Exception as e:
            return e

    def mclear(self, key: str):
        '''Clear all contents of a key'''
        try:
            d[key].clear()
            Lists.dataControl.changes(d)

            return True

        except KeyError as e:
            return False

        except Exception as e:
            return e

    def mdel(self, key: str):
        '''Delete a key from databse'''
        try:
            del d[key]
            Lists.dataControl.changes(d)

            return True

        except KeyError as e:
            return False

        except Exception as e:
            return e