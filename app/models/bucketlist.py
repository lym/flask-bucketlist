from datetime import datetime
import uuid
from tinydb import where

from .base_model import BaseModel


class Bucketlist(BaseModel):
    table_name = 'bucketlists'

    def __init__(
        self, title, description='', fulfilled=False
    ):
        # super().__init__()
        self.title = title
        self.description = description
        self.fulfilled = fulfilled

    @classmethod
    def create(cls, **kwargs):
        db_table = cls.db.table(cls.table_name)
        if kwargs is None or len(kwargs) == 0:
            return
        kwargs['created'] = datetime.now(cls.tz)
        kwargs['modified'] = datetime.now(cls.tz)
        for key, value in kwargs.items():
            kwargs[key] = value
        db_table.insert(
            {
                'id': int(uuid.uuid4()), 'data': kwargs
            }
        )

    @classmethod
    def delete(cls, _id):
        print('ID of Item for deletion'.format(_id))
        table = cls.db.table(cls.table_name)
        table.remove(where('id') == _id)

    @classmethod
    def all(cls):
        table = cls.db.table('bucketlists')
        return table.all()
