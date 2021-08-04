from django.db import models



class PhotoGallery(models.Model):
    label = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.label


class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=60)
    message = models.TextField(max_length=3000)
