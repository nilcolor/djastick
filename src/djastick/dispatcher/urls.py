# -*- coding: utf-8 -*-
from importlib import import_module
from django.conf.urls.defaults import patterns, include, url
from djastick.core.resources import Resource
from django.conf import settings

def dispatch(request, module, resource, **kwargs):
    """
    Main url dispatcher. Its only load resource and launch it.
    """
    module = import_module(module)
    resource = getattr(module, resource)
    
    return resource().__getattribute__(request.method.lower())(request, **kwargs)


def generate_urlpatterns():
    """
    No docstring yet
    """
    urlpatterns = patterns('')
    
    for app in settings.INSTALLED_APPS:
        module = app + '.resources'
        try:
            m = import_module(module)
        except ImportError:
            continue
        
        module_urls = []
        
        for attr_name in dir(m):
            attr = getattr(m, attr_name)
            
            if isinstance(attr, type) and issubclass(attr, Resource):
                urlpattern = attr.Meta.urlpattern #TODO replase with _meta attr
            else:
                continue
            
            if urlpattern:
                module_urls.append(url(urlpattern, dispatch,
                   {'module': module, 'resource': attr_name}, name=attr_name))
        
        module_patterns = patterns('', *module_urls)
        
        urlpatterns += patterns('',
            url('^', include((module_patterns, app, app)))
        )
    
    return urlpatterns


urlpatterns = generate_urlpatterns()
