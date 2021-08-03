from django.contrib import admin
from .models import PhotoGallery


class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = (
        'label',
        'image_url',
    )

    ordering = ('label',)

admin.site.register(PhotoGallery, PhotoGalleryAdmin)