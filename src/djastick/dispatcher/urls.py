# -*- coding: utf-8 -*-
from importlib import import_module
from django.conf.urls.defaults import patterns, url
from djastick.core import STATUS
from djastick.core.signals import security_should_check


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
    sec_results = security_should_check.send_robust(sender=None,
        request=request, module=module, resource=resource, mode=request.mode)

    try:
        module = import_module(module)
        resource = getattr(module, resource)
        handler = getattr(resource(), request.mode.lower())
    except Exception:

        return STATUS.NOT_IMPLEMENTED
    for secm, rc in sec_results:
        if not rc or isinstance(rc, Exception):
            return STATUS.FORBIDDEN
    
    return handler(request, **kwargs)
