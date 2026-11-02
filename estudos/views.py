from django.shortcuts import render

from .models import PlanoEstudo


def pagina(request):
    planos = PlanoEstudo.objects.prefetch_related('topicos')
    return render(request, 'estudos/pagina.html', {'planos': planos})
