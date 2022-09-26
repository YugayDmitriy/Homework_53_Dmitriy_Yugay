from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'created_at']
    list_filter = ['name']
    search_fields = ['name', 'status']
    fields = ['name', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Item, ItemAdmin)
