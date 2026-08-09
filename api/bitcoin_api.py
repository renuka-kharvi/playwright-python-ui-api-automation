from api.base_api import BaseAPI

class BitcoinAPI(BaseAPI):
    def __init__(self, request_context):
        super().__init__(request_context)
        self.request_context=request_context

    #-----------------------------------------------------
    # get Api request using baseapi function
    #-------------------------------------------------------
    def get_bitcoin(self,endpoint):
        return self.get_api(endpoint)
