from django.urls import path

from . import views

app_name = 'loguedje'
urlpatterns = [
    path('dico', views.dictionary, name='dictionary'),
    path('traducteur', views.translate, name='translate'),
]
