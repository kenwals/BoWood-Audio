from products.models import Product
from django.db import models
from django.db.models.fields import DecimalField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):

    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    userid = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=90)
    review_text = models.TextField(max_length=3000)


@receiver(post_save, sender=Review)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update products rating on review save/update 
    """
    if created: 
        print("a new review has been created")
    else:
        print("a current review has been updated")

@receiver(post_delete, sender=Review)
def update_on_delete(sender, instance, **kwargs):
    """
    Update products rating on review delete
    """
    print("a review has been deleted ")
