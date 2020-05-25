from flask_restful import Resource


class VersaoView(Resource):
    def get(self):
        return 'v1.1.1'
