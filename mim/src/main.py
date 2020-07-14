"""
    MimDB is database like Redis.
    It's a key value database.
    But in MimDB you can make columns.
    Im Mostafa Motahari and I started this project in Mondey 00:33
    For more details see my github and gitlab page:
    GitHub:
    GitLab:
"""

# Imports
from .data import database as d
from .connect import Connect
from .sets import Sets
from .lists import Lists
# End

class Mim(Sets, Lists, Connect):
    pass