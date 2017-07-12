from datetime import datetime
import pytz
from tinydb import TinyDB  # , Query
from tinydb.storages import MemoryStorage


class BaseModel:
    """ This class implements all our models' shared features """
    table_name = None
    tz = pytz.utc

    db = TinyDB(storage=MemoryStorage)

    def __init__(self):
        self.id = id(self)  # guaranteed uniqueness through one program session
        self.created = datetime.now(self.tz)
        self.modified = datetime.now(self.tz)
