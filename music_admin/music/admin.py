#coding=utf-8
from __future__ import absolute_import

from django.contrib import admin

from .models import AllFm,XMLYdpMeta
# Register your models here.

class AllFmAdmin(admin.ModelAdmin):
    fields = ('fm_name','url')


admin.site.register(
    AllFm,AllFmAdmin
)


admin.site.register(XMLYdpMeta)
