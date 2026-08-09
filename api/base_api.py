class BaseAPI:
    def __init__(self,request_context):
        self.request_context=request_context


    #-----------------------------------------------------
    # get Api request
    #-------------------------------------------------------
    def get_api(self,endpoints,**kwargs):
        return self.request_context.get(endpoints,**kwargs)

    #-----------------------------------------------------
    # post Api request
    #-------------------------------------------------------
    def post_api(self,endpoints,**kwargs):
        return self.request_context.post(endpoints,**kwargs)

    #-----------------------------------------------------
    # put Api request
    #-------------------------------------------------------
    def put_api(self,endpoints,**kwargs):
        return self.request_context.put(endpoints,**kwargs)

    #-----------------------------------------------------
    # patch Api request
    #-------------------------------------------------------
    def patch_api(self,endpoints,**kwargs):
        return self.request_context.patch(endpoints,**kwargs)
    #-----------------------------------------------------
    # delete Api request
    #-------------------------------------------------------
    def get_delete(self,endpoints,**kwargs):
        return self.request_context.delete(endpoints,**kwargs)

    