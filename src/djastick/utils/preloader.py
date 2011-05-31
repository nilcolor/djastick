# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.utils.importlib import import_module

def preload(*names):
    for app in settings.INSTALLED_APPS:
        m = import_module(app)
        for file in os.listdir(os.path.split(m.__file__)[0]):
            if file[-3:] == '.py' and file[:-3] in names:
                try:
                    import_module('.'+file[:-3], app)
                except DeprecationWarning:
                    pass
                except ImportError:
                    pass
