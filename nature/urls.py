from django.urls import path

from .views import NaturePageListView, NaturePageDetailView

app_name = 'nature'
urlpatterns = [
    path('', NaturePageListView.as_view(), name='index'),
    path('tag/<str:tag>', NaturePageListView.as_view(), name='tag'),
    path('page/<int:pk>', NaturePageDetailView.as_view(), name='page'),
]
