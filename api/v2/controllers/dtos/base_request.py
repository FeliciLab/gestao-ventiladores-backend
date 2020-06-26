class BaseRequest():
    def __init__(self, request):
        self.request = request
        self.method = request.method
        self.errors = []
        self.valid = None

    def validate(self):
        self.validate_format()
        self.validate_by_method()
        if self.valid == None:
            self.valid = True

    def valid(self):
        self.validate()
        return self.valid

    def body(self):
        if self.request.get_json() == None:
            self.add_error("No body found")
            return {}
        return self.request.get_json()

    def content(self):
        try: 
            return self.body()['content']
        except:
            self.add_error("No content found")
            return []
    
    def validate_format(self):
        if not type(self.content()) == self.EXPECTED_FORMAT:
            self.add_error("Unexpected format. {} was expected".format(str(self.EXPECTED_FORMAT)))

    def validate_by_method(self):
        if self.method == 'POST':
            self.validate_post()

    def validate_post(self):
        pass

    def add_error(self, error_message):
        self.valid = False
        self.errors.append(error_message)