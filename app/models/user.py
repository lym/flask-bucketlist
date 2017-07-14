from datetime import datetime
import uuid
import hashlib
from tinydb import where
from .base_model import BaseModel


class User(BaseModel):
    table_name = 'users'

    def __init__(
        self, email, password, first_name='', last_name='', username=''
    ):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = self._enc_passw(password)

    def _enc_passw(self, pw):
        safe_passw = pw.encode()
        msg = hashlib.sha256()
        msg.update(safe_passw)
        return msg

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
        table = cls.db.table('users')
        return table.all()
