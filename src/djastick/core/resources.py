# -*- coding: utf-8 -*-

class Resource(object):
    """
    Base Resourse
    """

    def get(self):
        raise NotImplementedError('Subclass must implements this method')

    def put(self):
        raise NotImplementedError('Subclass must implements this method')

    def post(self):
        raise NotImplementedError('Subclass must implements this method')

    def delete(self):
        raise NotImplementedError('Subclass must implements this method')

    class Meta:
        urlpattern = None
