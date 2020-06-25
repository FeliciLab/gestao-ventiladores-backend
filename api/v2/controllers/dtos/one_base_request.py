
class OneBaseRequest():
    def __init__(self, request):
        self.request = request
        self.errors = []
        self.valid = None

    def validate_post(self, item):
        if "_id" in item:
            self.add_error("ID must not be sent")