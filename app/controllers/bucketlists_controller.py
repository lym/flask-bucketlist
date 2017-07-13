from flask import (
    jsonify,
    request,
)
from flask.views import MethodView

from app.models import Bucketlist


class BucketlistsController(MethodView):
    def post(self):
        title = request.form.get('title')
        description = request.form.get('description')
        fulfilled = False
        Bucketlist.create(
            title=title, description=description, fulfilled=fulfilled
        )
        print('Title: {}\nDescription: {}'.format(title, description))
        print(request.form)
        res = {'Status': 'OK'}
        return jsonify(res)

    def get(self):
        bucketlists = jsonify(Bucketlist.all())
        return bucketlists
