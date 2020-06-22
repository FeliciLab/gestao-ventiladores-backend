from flask import make_response, jsonify
from http import HTTPStatus

def error_response(message, status=400):
    return make_response(
        jsonify({
            "error": message,
        }),
        status
    )


def get_response(content, deleted):
    response = {'content': content}

    response['deleted'] = True if deleted else False

    return make_response(jsonify(response), HTTPStatus.OK)


def post_response(content):
    return make_response(jsonify({'content': content}), 201)
