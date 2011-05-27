# -*- coding: utf-8 -*-
from djastick.core import STATUS


class Resource(object):
    """
    Base Resourse
    You can implement 4 methods:
        - get
        - put
        - post
        - delete
    I.e. something like this:
    
    >> def get(self):
    >>     return STATUS.NOT_IMPLEMENTED
    
    If method wasn't found by the url dispatcher - HTTP/501 NOT IMPLEMENTED will be returned to a client.
    """
    pass


