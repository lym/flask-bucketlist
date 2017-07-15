from tinydb import where

from app.models import (
    Bucketlist,
    Item,
    User
)

bucketlist = Bucketlist('New Bucketlist')
user = User('email@anonmail.com', 'weakpass')
item = Item('New Item', 118266162315588491253214850569623365886)


def test_default_attributes():
    assert bucketlist.table_name is not None

    assert item.id is not None
    assert item.created is not None
    assert item.modified is not None

    assert user.id is not None
    assert user.created is not None
    assert user.modified is not None


def test_bucketlist_create():
    """ It should create an bucketlist """
    title = 'Another one'
    description = 'Description for another one'
    table = bucketlist.db.table('bucketlists')
    len_before = len(table.all())

    Bucketlist.create(title=title, description=description)
    len_after = len(table.all())
    assert len(bucketlist.db.table(bucketlist.table_name).all()) != 0
    assert len_before != len_after


def test_user_create():
    """ It should create a new user """
    email = 'lym@lym.com'
    passw = 'lympass'
    table = user.db.table('users')
    len_before = len(table.all())

    User.create(email=email, password=passw)
    len_after = len(table.all())
    assert len(user.db.table(user.table_name).all()) != 0
    assert len_before != len_after


def test_create_item():
    """It should create an item """
    title = 'New Item'
    bucketlist_id = item.bucketlist
    table = item.db.table('items')
    len_before = len(table.all())
    assert len_before == 0, 'No items yet'

    Item.create(title=title, bucketlist_id=bucketlist_id)
    len_after = len(table.all())
    assert len(table.all()) != 0, 'Expected at least one item in the items table'  # NOQA
    assert len_before != len_after
    assert len(item.db.table(item.table_name).all()) != 0
    assert len_before != len_after


def test_presence_of_table_names():
    """ Models should have table names """

    assert bucketlist.table_name is not None
    assert user.table_name is not None
    assert item.table_name is not None


def test_delete_user():
    """ It should delete a User instance from the database """
    email = 'lym@lym.com'
    passw = 'lympass'
    table = user.db.table('users')
    User.create(email=email, password=passw)

    len_before = len(table.all())
    rec_id = table.all()[-1].get('id')  # Get last-saved item
    User.delete(rec_id)
    len_after = len(table.all())
    found = table.get(where('id') == rec_id)
    assert found is None
    assert len_before != len_after


def test_delete_bucketlist():
    """ It should delete a bucket list instance from the bucketlists table """
    title = 'Item for deletion'
    table = bucketlist.db.table(bucketlist.table_name)
    Bucketlist.create(
        title=title,
        description='This item is meant to test the delete functionality'
    )
    len_before = len(table.all())
    assert len_before != 0

    rec_id = table.all()[-1].get('id')
    Bucketlist.delete(rec_id)
    len_after = len(table.all())
    found = table.get(where('id') == rec_id)
    assert found is None
    assert len_before != len_after


def test_delete_item():
    title = 'Item for deletion'
    table = item.db.table('items')
    Item.create(title=title)
    len_before = len(table.all())
    assert len_before != 0

    rec_id = table.all()[-1].get('id')  # Get last-saved item
    Item.delete(rec_id)
    len_after = len(table.all())
    found = table.get(where('id') == rec_id)
    assert found is None
    assert len_before != len_after
