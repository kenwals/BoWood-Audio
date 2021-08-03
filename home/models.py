from django.db import models



class PhotoGallery(models.Model):
    label = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.label