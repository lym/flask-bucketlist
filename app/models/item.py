from datetime import datetime
import uuid
from tinydb import where
from .base_model import BaseModel


class Item(BaseModel):
    table_name = 'items'

    def __init__(self, title, bucketlist_id, description='', fulfilled=False):
        super().__init__()
        self.title = title
        self.description = description
        self.fulfilled = fulfilled
        self.bucketlist = bucketlist_id

    @classmethod
    def create(cls, **kwargs):
        print('Arguments dictionary: {}'.format(kwargs))
        db_table = cls.db.table(cls.table_name)
        if (kwargs is None) or (kwargs.get('bucketlist_id') is None):
            return
        if (kwargs.get('start_date') is None) or len(kwargs.get('start_date')) == 0:  # NOQA
            kwargs['start_date'] = datetime.now(cls.tz)
        if (kwargs.get('due_date') is None) or len(kwargs.get('due_date')) == 0:  # NOQA
            kwargs['due_date'] = None
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
        table = cls.db.table('items')
        return table.all()
