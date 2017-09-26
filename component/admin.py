from django.contrib import admin
from component.models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display=['name','get_status_display']


admin.site.register(Application, ApplicationAdmin)