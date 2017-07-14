from flask import (
    jsonify,
    request,
)
from flask.views import MethodView
from tinydb import where

from app.models import Item


class ItemsController(MethodView):
    def post(self):
        title = request.form.get('title')
        description = request.form.get('description')
        fulfilled = False
        bucketlist_id = request.form.get('bucketlist_id')
        Item.create(
            title=title, bucketlist=bucketlist_id, description=description,
            fulfilled=fulfilled
        )
        res = {'Status': 'OK'}
        return jsonify(res)

    def get(self):
        if request.args.get('item') is not None:
            bucketlist_id = int(request.args.get('item'))
            table = Item.db.table('bucketlists')
            result = table.get(where('id') == bucketlist_id)
            if result is None:
                return jsonify({})
            return jsonify(result)
        items = jsonify(Item.all())
        return items
