# -*- coding: utf-8 -*-
from django.http import HttpResponse
# from utils.enum import Enum, EnumItem

class status_factory(object):
    """
    Status codes.
    """
    
    # class CODES(Enum):
    #     OK = EnumItem(200, "OK")
    #     CREATED = EnumItem(201, 'Created')
    #     DELETED = EnumItem(204, '') # The 204 response MUST NOT include a message-body, and thus is always terminated by the first empty line after the header fields.
    #     BAD_REQUEST = EnumItem(400, 'Bad Request')
    #     UNAUTHORIZED = EnumItem(401, 'Unauthorized')
    #     FORBIDDEN = EnumItem(403, 'Forbidden')
    #     NOT_FOUND = EnumItem(404, 'Not Found')
    #     METHOD_NOT_ALLOWED = EnumItem(405, 'Method Not Allowed')
    #     CONFLICT_ENTRY = EnumItem(409, 'Conflict')
    #     GONE = EnumItem(410, 'Gone')
    #     INTERNAL_ERROR = EnumItem(500, 'Internal Error')
    #     NOT_IMPLEMENTED = EnumItem(501, 'Not Implemented')
    
    CODES = dict(
        OK = (200, "OK"),
        CREATED = (201, 'Created'),
        DELETED = (204, ''), # The 204 response MUST NOT include a message-body, and thus is always terminated by the first empty line after the header fields.
        BAD_REQUEST = (400, 'Bad Request'),
        UNAUTHORIZED = (401, 'Unauthorized'),
        FORBIDDEN = (403, 'Forbidden'),
        NOT_FOUND = (404, 'Not Found'),
        METHOD_NOT_ALLOWED = (405, 'Method Not Allowed'),
        CONFLICT_ENTRY = (409, 'Conflict'),
        GONE = (410, 'Gone'),
        INTERNAL_ERROR = (500, 'Internal Error'),
        NOT_IMPLEMENTED = (501, 'Not Implemented'),
    )
    def __getattr__(self, attr):
        try:
            (r, c) = self.CODES.get(attr)
        except TypeError:
            raise AttributeError(attr)
        
        class HttpResponseWrapper(HttpResponse):
            def _set_content(self, content):
                """
                http://code.djangoproject.com/ticket/9403 
                """
                if not isinstance(content, basestring) and hasattr(content, '__iter__'):
                    self._container = content
                    self._is_string = False
                else:
                    self._container = [content]
                    self._is_string = True
            
            content = property(HttpResponse._get_content, _set_content)
        
        return HttpResponseWrapper(c, content_type='text/plain', status=r)


STATUS = status_factory()