from products.models import Product
from django.db import models
from django.db.models.fields import DecimalField

from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):

    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    userid = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=90)
    review_text = models.TextField(max_length=3000)

