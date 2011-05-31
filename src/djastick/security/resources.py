# -*- coding: utf-8 -*-
from django.db.models.query_utils import Q
from django.dispatch.dispatcher import receiver
from djastick.core.resources import Resource
from djastick.core.signals import security_should_check
from djastick.security.models import ResourceAccessNode

ProtectedResourceRegistry = set()


class ProtectedResourceMetaclass(type):
    def __new__(mcs, name, bases, dict):
        resource = '%s.%s' % (dict['__module__'], name)
        if resource != 'djastick.security.resources.ProtectedResource':
            ProtectedResourceRegistry.add(resource)
        return type.__new__(mcs, name, bases, dict)


class ProtectedResource(Resource):
    __metaclass__ = ProtectedResourceMetaclass
    pass



@receiver(security_should_check)
def check_acl(sender, request, module, resource, mode, **kwargs):

    q = {
        'GET': Q(get=True),
        'PUT': Q(put=True),
        'POST': Q(post=True),
        'DELETE': Q(delete=True),
    }
    if mode not in q:
        return False

    nodes = ResourceAccessNode.objects.filter(
                    resource='%s.%s' % (module, resource),
                    acl__group__in=request.user.groups.all()).filter(q[mode])

    return nodes.count()
