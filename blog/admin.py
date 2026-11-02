from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from .models import Post, PostMedia


class PostMediaInline(TabularInline):
    model = PostMedia
    extra = 1
    fields = ('arquivo', 'legenda', 'snippet')
    readonly_fields = ('snippet',)

    @admin.display(description='Cole no conteúdo')
    def snippet(self, obj):
        return f'![{obj.legenda}]({obj.nome})' if obj.pk else 'Salve para gerar'


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('titulo', 'publicado', 'publicado_em')
    list_filter = ('publicado',)
    search_fields = ('titulo', 'resumo')
    prepopulated_fields = {'slug': ('titulo',)}
    inlines = [PostMediaInline]
