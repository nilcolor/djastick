# -*- coding: utf-8 -*-
from django.http import HttpResponse
from djastick.core.resources import Resource

class GoodsListResource(Resource):
    """
    List of goods.
    """

    def launch(self, request):
        return HttpResponse('Hallo djastick!!!')

    def get(self):
        pass
    
    class Meta:
        urlpattern = r'^$'

