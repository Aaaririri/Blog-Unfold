from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline, TabularInline

from .models import Curriculo, Experiencia, Formacao, Habilidade, ProjetoCurriculo


class ExperienciaInline(StackedInline):
    model = Experiencia
    extra = 0


class FormacaoInline(TabularInline):
    model = Formacao
    extra = 0


class HabilidadeInline(TabularInline):
    model = Habilidade
    extra = 0


class ProjetoInline(StackedInline):
    model = ProjetoCurriculo
    extra = 0


@admin.register(Curriculo)
class CurriculoAdmin(ModelAdmin):
    inlines = [ExperienciaInline, FormacaoInline, HabilidadeInline, ProjetoInline]

    def has_add_permission(self, request):
        return not Curriculo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
