from django.urls import path

from . import views

app_name = 'kapnoc_pages'
urlpatterns = [
    path('image/<str:name>', views.get_image_by_name, name='image_by_name'),
    path('image/md_uploader/', views.markdown_uploader,
         name='markdown_uploader_page'),
]
