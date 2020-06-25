
class BaseRequest():
    def __init__(self, request):
        self.method = request.method
        self.body = request.get_json()
        self.errors = []
        self.valid = None

    def validate(self):
        self.validate_format()
        self.validate_by_method()
        if self.valid == None:
            self.valid = True

    def content(self):
        try: 
            return self.body['content']
        except:
            self.__add_error("No content found")
            return []
    
    def validate_format(self):
        if not type(self.content()) == self.EXPECTED_FORMAT:
            self.__add_error("Unexpected format. {} was expected".format(str(self.EXPECTED_FORMAT)))

    def validate_by_method(self):
        if self.method == 'POST':
            self.validate_post()

    def validate_post(self):
        for index, item in enumerate(self.content()):
            if "_id" in item:
                self.__add_error("ID must not be sent")

    def __add_error(self, error_message):
        self.valid = False
        self.errors.append(error_message)