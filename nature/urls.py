from django.urls import path

from . import views

app_name = 'nature'
urlpatterns = [
    path('', views.index, name='index'),
    path('tag/<int:pk>', views.tag_pk, name='tag_pk'),
    path('tag/<str:name>', views.tag_name, name='tag_name'),
    path('page/<int:pk>', views.page, name='page'),
]
