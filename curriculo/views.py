from django.shortcuts import render

from .models import Curriculo


def pagina(request):
    return render(request, 'curriculo/pagina.html', {'c': Curriculo.objects.first()})
