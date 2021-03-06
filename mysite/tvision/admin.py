# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import reverse

from .models import AutomatedPage, ReleasePage, BugPage
from .models import AutomatedDocument, ReleaseDocument, BugDocument
from .models import AutomatedLink, ReleaseLink, BugLink

from django.utils.html import format_html

# Register your models here.
admin.site.register(AutomatedPage)
admin.site.register(ReleasePage)
admin.site.register(BugPage)
admin.site.register(AutomatedLink)
admin.site.register(ReleaseLink)
admin.site.register(BugLink)
admin.site.register(AutomatedDocument)
admin.site.register(ReleaseDocument)
admin.site.register(BugDocument)

class PersonalAdmin(AdminSite):
    site_header = "T|Vision Adminstration"

admin_site = PersonalAdmin(name='myadmin')
admin_site.register(AutomatedPage)
admin_site.register(ReleasePage)
admin_site.register(BugPage)
admin_site.register(AutomatedLink)
admin_site.register(ReleaseLink)
admin_site.register(BugLink)
admin_site.register(AutomatedDocument)
admin_site.register(ReleaseDocument)
admin_site.register(BugDocument)

class AdminLink(admin.ModelAdmin):
    list_display = [
        "pub_date",
        "author",
        "title",
        "precondition",
        "steps",
        "parameters",
        "comments",
        "upload",
        "link_from_auto",
        "link_from_release",
        "link_from_bug"
        ]
    def link_from_auto(self,obj):
        link = urlresolvers.reverse("admin:tvision_autolink_change",args=[obj.AutomatedLink.id])
        return '<a href="%s">%s</a>' % (obj.AutomatedLink.url,obj.AutomatedLink.url)
    def link_from_release(self,obj):
        link = urlresolvers.reverse("admin:tvision_autolink_change",args=[obj.releaselink.id])
        return '<a href="%s">%s</a>' % (obj.ReleaseLink.url,obj.ReleaseLink.url)
    def link_from_bug(self,obj):
        link = urlresolvers.reverse("admin:tvision_autolink_change",args=[obj.BugLink.id])
        return '<a href="%s">%s</a>' % (obj.BugLink.url,obj.BugLink.url)
    link_from_auto.allow_tags=True
    link_from_release.allow_tags=True
    link_from_bug.allow_tags=True
