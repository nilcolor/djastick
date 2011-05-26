# -*- coding: utf-8 -*-
from importlib import import_module
from django.conf.urls.defaults import patterns, url

def urn(regex, resource, name, module=None):
    """
    Helper for RegexURLPattern creation.
    Same as django "url", but works with dispatcher instead of simple view.
    """
    return url(regex, dispatch, {'module': module, 'resource': resource}, name=name)


def urnpatterns(module, *urlparams):
    """
    Helper for "patterns" creation.
    Same as django "patterns", but works with dispatcher instead of simple view.
    """
    for url in urlparams:
        url.default_args.update({'module': module})
    return patterns('', *urlparams)


def dispatch(request, module, resource, **kwargs):
    """
    Main url dispatcher. Its only load resource and launch it.
    """
    module = import_module(module)
    resource = getattr(module, resource)
    method = request.method.lower()
    return getattr(resource(), method)(request, **kwargs)
