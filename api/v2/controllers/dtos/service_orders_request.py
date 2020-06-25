from .many_request import ManyRequest

class ServiceOrdersRequest(ManyRequest):
    
    def validate(self):
        print("EAI")
        super().validate()
        print("valeu")
        # here goes the service order specific validation
    