# -*- coding: utf-8 -*-
from django.http import HttpResponse
from djastick.core.resources import Resource

class GoodsListResource(Resource):
    """
    List of goods.
    """
    def get(self, request):
        from djastick.core import STATUS
        
        # return HttpResponse('Hallo djastick!!!')
        return STATUS.NOT_IMPLEMENTED


class GoodsListResource(Resource):
    """
    List of goods.
    """
    def get(self, request):
        from djastick.core import STATUS
        
        return HttpResponse('Hallo djastick!!!')
        # return STATUS.NOT_IMPLEMENTED


