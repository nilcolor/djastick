# -*- coding: utf-8 -*-
from django.http import HttpResponse
from djastick.core.resources import Resource

class GoodsListResource(Resource):
    """
    List of goods.
    """
    class Meta:
        urlpattern = r'^$'
    
    def launch(self, request):
        return HttpResponse('Hallo djastick!!!')
    
    def get(self, request):
        from djastick.core import STATUS
        
        return STATUS.NOT_IMPLEMENTED


