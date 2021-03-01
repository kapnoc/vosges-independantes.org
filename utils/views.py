import json
import uuid

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, Http404
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files import File
from django.urls import reverse
from django.utils.text import slugify
from photologue.models import Photo
from martor.utils import LazyEncoder

# Create your views here.


def get_photo_display_by_slug(request, slug):
    photo = get_object_or_404(Photo, slug=slug)
    return redirect(photo.get_display_url())


def get_photo_thumbnail_by_slug(request, slug):
    photo = get_object_or_404(Photo, slug=slug)
    return redirect(photo.get_thumbnail_url())


@ login_required
def markdown_uploader(request):
    """
    Markdown image upload to Image db object (using default storage)
    and represent as json for markdown editor.
    """
    if request.method == 'POST' and request.is_ajax():
        if 'markdown-image-upload' in request.FILES:
            image = request.FILES['markdown-image-upload']
            image_types = [
                'image/png', 'image/jpg',
                'image/jpeg', 'image/pjpeg', 'image/gif'
            ]
            if image.content_type not in image_types:
                data = json.dumps({
                    'status': 405,
                    'error': _('Bad image format.')
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

            if image.size > settings.MAX_IMAGE_UPLOAD_SIZE:
                to_MB = settings.MAX_IMAGE_UPLOAD_SIZE / (1024 * 1024)
                data = json.dumps({
                    'status': 405,
                    'error': _('Maximum image file is %(size) MB.') % {'size': to_MB}
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

            slug = "{0}-{1}".format(
                uuid.uuid4().hex[:10], slugify(image.name))
            photo_db = Photo(
                image=image,
                title=slug,
                slug=slug,
            )
            photo_db.save()

            image_url = reverse(
                'utils:photo_display_by_slug', args=[photo_db.slug])

            data = json.dumps({
                'status': 200,
                'link': image_url,
                'name': photo_db.title
            })
            return HttpResponse(data, content_type='application/json')
        return HttpResponse(_('Invalid request!'))
    return HttpResponse(_('Invalid request!'))
