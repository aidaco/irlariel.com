# Aidan Courtney 2020, see incl. license for details.

from .dbi import DBInterface

def connect(path: str):
    # TODO docs
    # ? attempt to connect to the database and return the connection

    return DBInterface(path)