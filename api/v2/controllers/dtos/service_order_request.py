class ServiceOrderRequest:
    def __init__(self, data):
        self.tipo = data["tipo"]
        self.data = data

    def get(self):
        return self.data

    def valid(self):
        return True

    def errors(self):
        return [{}]
