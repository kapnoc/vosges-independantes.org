import os
import json
import uuid

from django.conf import settings
from django.http import HttpResponse, Http404
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files import File
from martor.utils import LazyEncoder
from django.urls import reverse
from django.shortcuts import redirect

from .models import Image


def get_image_by_name(request, name):
    try:
        image = Image.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Http404('Image does not exist')
    return redirect(image.contents.url)


@login_required
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

            # ALED
            image_uuid = "{0}-{1}".format(
                uuid.uuid4().hex[:10], image.name.replace(' ', '-'))
            image_db = Image(name=image_uuid,
                             description=image.name, contents=image)
            image_db.save()
            image_url = reverse(
                'kapnoc_pages:image_by_name', args=[image_db.name])

            data = json.dumps({
                'status': 200,
                'link': image_url,
                'name': image_db.name
            })
            return HttpResponse(data, content_type='application/json')
        return HttpResponse(_('Invalid request!'))
    return HttpResponse(_('Invalid request!'))
