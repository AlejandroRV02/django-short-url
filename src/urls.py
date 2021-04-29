from django.urls import path
from .views import CrearAcortador,PaginaEnlace,RedirectEnlace

app_name= 'src'

urlpatterns = [

    path('', CrearAcortador.as_view(), name='index'),
    path('<int:pk>/', PaginaEnlace.as_view(), name='enlace'),
    path('<str:codigo>/', RedirectEnlace.as_view(), name='redirect'),
]