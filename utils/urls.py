from django.urls import path
from .views import (get_photo_display_by_slug,
                    get_photo_thumbnail_by_slug, markdown_uploader)

app_name = "utils"
urlpatterns = [
    path('display/<slug:slug>', get_photo_display_by_slug,
         name='photo_display_by_slug'),
    path('thumb/<slug:slug>', get_photo_thumbnail_by_slug,
         name='photo_thumbnail_by_slug'),
    path('image/md_uploader/', markdown_uploader,
         name='markdown_uploader'),
]
