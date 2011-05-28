# encoding: utf-8
import re
import itertools
from django.utils import simplejson as json


class HttpMethodsOverride(object):
    """
    Method override based on <.. name="_method" value="put" /> elements.
    Used to deal with current browser limitation.
    Don't necessary if you can use true PUT/DELETE methods.
    """
    SUPPORTED_TRANSFORMS = ['POST','PUT', 'DELETE']
    MIDDLEWARE_KEY = '_method'
    
    def process_request(self, request):
        setattr(request, 'mode', request.method) # anyway i need a `mode` attribute
        if request.POST and request.POST.has_key(self.MIDDLEWARE_KEY):
            if request.POST[self.MIDDLEWARE_KEY].upper() in self.SUPPORTED_TRANSFORMS:
                # nice way but broke Django...
                # request.method = request.POST[self.MIDDLEWARE_KEY].upper()
                setattr(request, 'mode', request.POST)
                # setattr(request, request.method, request.POST)
        
        return None


class BodyDecoder(object):
    """
    Decodes request body and save it as the requests `body` attribute.
    Known types decoded. Unknown saves as-is.
    """
    def __init__(self):
        # List of known decoders:
        self.decoders = {
            'application/json': self.decodeJSON,
        }
    
    def process_request(self, request):
        body = request.read()
        setattr(request, 'body', self.decoders.get(request.META['CONTENT_TYPE'], self._defaultDecoder)(body))
        print "============================================"
        print request.body
        print "============================================"
        return None
    
    def _defaultDecoder(self, data):
        return data
    
    def decodeJSON(self, data):
        """
        Decodes JSON request body
        """
        return json.loads(data)