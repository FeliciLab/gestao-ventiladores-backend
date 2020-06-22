from flask_restful import Resource


class VersaoView(Resource):
    def get(self):
        return 'v2.0.0-dev'
