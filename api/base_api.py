from utils.logger import get_logger
class BaseAPI:
    def __init__(self,request_context):
        self.request_context=request_context
        self.logger=get_logger(__name__)


    #-----------------------------------------------------
    # get Api request
    #-------------------------------------------------------
    def get_api(self,endpoint,**kwargs):
        try:
            self.logger.info(f"GET Request: {endpoint}")
        
            response= self.request_context.get(endpoint,**kwargs)

            self.logger.info(f"GET Response: {response.status}")
            return response
        except Exception as error:

            self.logger.error(f"GET request failed: "f"{endpoint} | {error}")

            # Re-raise so Pytest detects the failure.
            raise


    #-----------------------------------------------------
    # post Api request
    #-------------------------------------------------------
    def post_api(self,endpoint,**kwargs):
        try:
            self.logger.info(f"POST Request: {endpoint}")

            response= self.request_context.post(endpoint,**kwargs)
            self.logger.info(f"POST Response: {response.status}")

            return response
        except Exception as error:

            self.logger.error(f"POST request failed: "f"{endpoint} | {error}")

            raise

    #-----------------------------------------------------
    # put Api request
    #-------------------------------------------------------
    def put_api(self,endpoint,**kwargs):
        try:
            self.logger.info(f"PUT Request: {endpoint}")

            response= self.request_context.put(endpoint,**kwargs)
            self.logger.info(f"PUT Response: {response.status}")

            return response
        except Exception as error:

            self.logger.error(f"PUT request failed: "f"{endpoint} | {error}")

            raise

    #-----------------------------------------------------
    # patch Api request
    #-------------------------------------------------------
    def patch_api(self,endpoint,**kwargs):
        try:
            self.logger.info(f"PATCH Request: {endpoint}")

            response= self.request_context.patch(endpoint,**kwargs)
            self.logger.info(f"PUT Response: {response.status}")
            
            return response
        except Exception as error:
            self.logger.error(f"PATCH request failed: "f"{endpoint} | {error}")
            
            raise
            
    #-----------------------------------------------------
    # delete Api request
    #-------------------------------------------------------
    def get_delete(self,endpoint,**kwargs):
        try:

            self.logger.info(f"DELETE Request: {endpoint}")

            response= self.request_context.delete(endpoint,**kwargs)
            self.logger.info(f"DELETE Response: {response.status}")

            return response

        except Exception as error:

            self.logger.error(f"DELETE request failed: "f"{endpoint} | {error}" )

            raise

    