# -*- coding: utf-8 -*-
from django.http import HttpResponse
from djastick.core.resources import Resource
from djastick.security.resources import ProtectedResource

class GoodsListResource(ProtectedResource):
    """
    List of goods.
    """
    def get(self, request):
        from djastick.core import STATUS
        return HttpResponse('Hallo djastick!!!')
        # return STATUS.NOT_IMPLEMENTED
        
    def delete(self, request):
        """docstring for delete"""
        return HttpResponse('You just deleted djastick!!!')


