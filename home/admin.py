# home/admin.py
from django.contrib import admin
from .models import News, TrackLayout

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'author', 'created_at')
    search_fields = ('headline', 'content')
    ordering = ('-created_at',)


@admin.register(TrackLayout)
class TrackLayoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)