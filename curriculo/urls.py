from django.urls import path

from . import views

app_name = 'curriculo'
urlpatterns = [path('curriculo/', views.pagina, name='pagina')]
