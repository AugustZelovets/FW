from django.contrib import admin

from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'time_create', 'time_update', 'is_published', 'cat'

    list_display_links = 'id', 'title'
    search_fields = 'title', 'content'
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    list_display_links = 'name',
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Women, WomenAdmin)
