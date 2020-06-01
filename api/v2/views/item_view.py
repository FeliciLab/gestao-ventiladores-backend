from flask_restful import Resource
from flask import jsonify


class ItemMany(Resource):
    def get(self):
        return jsonify([{'msg': 'ok', 'deleted_at': 'asasa'}])