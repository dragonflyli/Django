from django.contrib import admin

from .models import Block


class BlockAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "manager", "status")

admin.site.register(Block, BlockAdmin)
