from django.contrib import admin

from manager_app.models import ManagerItem


@admin.register(ManagerItem)
class ManagerItemAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'done'
    list_display_links = 'id', 'title'
