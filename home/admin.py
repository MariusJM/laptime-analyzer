# home/admin.py
from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'author', 'created_at')
    search_fields = ('headline', 'content')
    ordering = ('-created_at',)
