# encoding: utf-8

import re
import itertools

class HttpMethodsOverride(object):
    """
    Method override based on <.. name="_method" value="put" /> elements.
    Used to deal with current browser limitation.
    Don't necessary if you can use true PUT/DELETE methods.
    """
    SUPPORTED_TRANSFORMS = ['POST','PUT', 'DELETE']
    MIDDLEWARE_KEY = '_method'
    
    def process_request(self, request):
        if request.POST and request.POST.has_key(self.MIDDLEWARE_KEY):
            if request.POST[self.MIDDLEWARE_KEY].upper() in self.SUPPORTED_TRANSFORMS:
                request.method = request.POST[self.MIDDLEWARE_KEY].upper()
        else:
            request.method = 'GET'
        
        print request.method
        
        return None


