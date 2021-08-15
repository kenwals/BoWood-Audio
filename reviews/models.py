from products.models import Product, UserProfile
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.db.models import Avg
from django.dispatch import receiver


class Review(models.Model):

    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    userid = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=90)
    review_text = models.TextField()

    def __str__(self):
        return self.name


@receiver(post_save, sender=Review)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update products rating on review save/update
    """
    product = Product.objects.get(name=instance.product)
    reviews = Review.objects.filter(product=product)
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    product.rating = int(avg_rating)
    product.save()


@receiver(post_delete, sender=Review)
def update_on_delete(sender, instance, **kwargs):
    """
    Update products rating on review delete
    """
    product = Product.objects.get(name=instance.product)
    reviews = Review.objects.filter(product=product)
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    if avg_rating:
        product.rating = int(avg_rating)
    else:
        product.rating = 0
    product.save()
