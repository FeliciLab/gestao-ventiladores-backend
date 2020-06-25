from .many_request import ManyRequest

class ServiceOrdersRequest(ManyRequest):
    
    def validate(self):
        super().validate()
    