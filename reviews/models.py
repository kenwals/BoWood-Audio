from products.models import Product
from django.db import models
from django.db.models.fields import DecimalField

from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):

    rating = models.IntegerField()
    userid = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=90)
    review_text = models.CharField(max_length=3000)

