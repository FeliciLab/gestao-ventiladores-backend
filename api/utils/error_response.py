from flask import make_response, jsonify


def error_response(message, status=400):
    return make_response(
        jsonify({
            "error": True,
            "message": message
        }),
        status
    )
