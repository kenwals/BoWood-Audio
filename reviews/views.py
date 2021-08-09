from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile

# Create your views here.

def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_form = form.save(commit=False)
            review_form.userid = UserProfile.objects.get(user=request.user)
            review_form.product = product
            print(review_form)
            review_form.save()
            messages.success(request, "Your review has been added now")
        else:
            messages.error(request, 'Failed to add review, please ensure form is valid.')
    else:
        form = ReviewForm()
    reviews = Review.objects.filter(product=product_id)

    context = {
            'product': product,
            'reviews': reviews,
            'review_form': form,
    }

    return render(request, 'products/product_detail.html', context)
