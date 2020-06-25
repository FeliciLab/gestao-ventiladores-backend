from .base_request import BaseRequest

class ManyRequest(BaseRequest):
    EXPECTED_FORMAT = list

    def validate_post(self):
        for index, item in enumerate(self.content()):
            if "_id" in item:
                self.add_error("ID must not be sent")

