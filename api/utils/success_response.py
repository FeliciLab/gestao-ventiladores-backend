from flask import make_response, jsonify
from http import HTTPStatus


def post_response(content):
    return make_response(jsonify({"content": content}), 201)
