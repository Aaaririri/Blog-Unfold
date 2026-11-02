from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline

from .models import PlanoEstudo, Topico


class TopicoInline(StackedInline):
    model = Topico
    extra = 1


@admin.register(PlanoEstudo)
class PlanoEstudoAdmin(ModelAdmin):
    list_display = ('titulo', 'ordem', 'progresso_total')
    inlines = [TopicoInline]

    @admin.display(description='progresso')
    def progresso_total(self, obj):
        return f'{obj.progresso()}%'
