# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

class ResourceAccessNode(models.Model):
    acl = models.ForeignKey('ResourceACL')
    resource = models.CharField(max_length=150)
    get = models.BooleanField()
    put = models.BooleanField()
    post = models.BooleanField()
    delete = models.BooleanField()

    def __unicode__(self):
        return self.resource


class ResourceACL(models.Model):
    group = models.OneToOneField('auth.Group')

    def __unicode__(self):
        return u'ResourceACL for "%s"' % self.group


@receiver(post_save, sender=ResourceACL)
def create_access_nodes(sender, instance, created, **kw):
    from djastick.security.resources import ProtectedResourceRegistry
    if created:
        for resource in ProtectedResourceRegistry:
            ResourceAccessNode.objects.get_or_create(acl=instance,
                                                            resource=resource)
