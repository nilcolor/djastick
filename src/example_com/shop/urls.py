# -*- coding: utf-8 -*-
from djastick.dispatcher.urls import urn, urnpatterns

urlpatterns = urnpatterns('example_com.shop.resources',
    urn(r'^$', 'GoodsListResource', name='GoodsList'),
)
