# -*- coding: utf-8 -*-

from django.contrib import admin
from djastick.security.models import ResourceAccessNode, ResourceACL


class ResourceAccessNodeInline(admin.TabularInline):
    model = ResourceAccessNode
    extra = 0
    can_delete = False
    fields = 'resource', 'get', 'put', 'post', 'delete'
    readonly_fields = ['resource']


class ResourceACLAdmin(admin.ModelAdmin):
    inlines = [ResourceAccessNodeInline]

admin.site.register(ResourceACL, ResourceACLAdmin)
