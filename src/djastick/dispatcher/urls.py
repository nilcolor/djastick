# -*- coding: utf-8 -*-
from importlib import import_module
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from djastick.core.resources import Resource
from django.dispatch import Signal

from djastick.core import STATUS


security_should_check = Signal(providing_args=["module", "resource", "mode"])

def dispatch(request, module, resource, **kwargs):
    """
    Main url dispatcher. Its only load resource and launch it.
    """
    try:
        module = import_module(module)
        resource = getattr(module, resource)
        handler = resource().__getattribute__(request.mode.lower())
    except Exception:
        return STATUS.NOT_IMPLEMENTED
    
    #send security signal
    sec_results = security_should_check.send_robust(sender=None, module=module, resource=resource, mode=request.mode)
    print sec_results
    #here i have sec check results. and i can behave like sentinel ;)
    for secm, rc in sec_results:
        if not rc: # i decide to ignore listener's exceptions... who cares about bad listeners? it's not my fault.
            return STATUS.FORBIDDEN
    
    return handler(request, **kwargs)


# some sample/dummy security modules. simple but they works.
def dummy_security(sender, **kwargs):
    print "C'mon! It's free for all day!"
    return True

security_should_check.connect(dummy_security)


def bad_security(sender, **kwargs):
    print "Yeah... i'm really bad. My dev was drunk. Sorry"
    lvar = 23 / 0
    
    return False

security_should_check.connect(bad_security)


def ro_system(sender, **kwargs):
    print "No DELETE please"
    
    return kwargs['mode'] != 'DELETE'

security_should_check.connect(ro_system)





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
                module_urls.append( url(urlpattern, dispatch, {'module': module, 'resource': attr_name}, name=attr_name) )
        
        module_patterns = patterns('', *module_urls)
        
        urlpatterns += patterns('',
            url('^', include((module_patterns, app, app)))
        )
    
    return urlpatterns


urlpatterns = generate_urlpatterns()
