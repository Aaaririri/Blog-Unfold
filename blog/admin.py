from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Post


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('titulo', 'publicado', 'publicado_em')
    list_filter = ('publicado',)
    search_fields = ('titulo', 'resumo')
    prepopulated_fields = {'slug': ('titulo',)}
