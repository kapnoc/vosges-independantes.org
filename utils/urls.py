from django.urls import path
from .views import (get_photo_original_by_slug,
                    get_photo_SIZE_by_slug, markdown_uploader)

app_name = "utils"
urlpatterns = [
    path('photo/<slug:slug>', get_photo_original_by_slug,
         name='photo_original_by_slug'),
    path('photo/<slug:slug>/<str:size>', get_photo_SIZE_by_slug,
         name='photo_SIZE_by_slug'),
    path('md_uploader/', markdown_uploader,
         name='markdown_uploader'),
]
