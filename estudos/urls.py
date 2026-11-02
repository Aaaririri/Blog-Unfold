from django.urls import path

from . import views

app_name = 'estudos'
urlpatterns = [path('estudos/', views.pagina, name='pagina')]
