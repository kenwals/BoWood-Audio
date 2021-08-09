from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_form = form.save(commit=False)
            review_form.userid = UserProfile.objects.get(user=request.user)
            review_form.product = product
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

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been edited now")
        else:
            messages.error(request, 'Failed to edit review, please ensure form is valid.')
    product = review.product
    reviews = Review.objects.filter(product=product)
    form = ReviewForm()
    context = {
            'product': product,
            'reviews': reviews,
            'review_form': form,
    }
    return render(request, 'products/product_detail.html', context)

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    product = review.product
    review.delete()
    messages.success(request, "Your review has been deleted now")
    reviews = Review.objects.filter(product=product)
    form = ReviewForm()
    context = {
            'product': product,
            'reviews': reviews,
            'review_form': form,
    }
    return render(request, 'products/product_detail.html', context)