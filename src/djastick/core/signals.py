# -*- coding: utf-8 -*-
from django.dispatch.dispatcher import Signal

security_should_check = Signal(providing_args=["request", "module", "resource", "mode"])
