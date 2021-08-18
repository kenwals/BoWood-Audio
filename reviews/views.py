from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)
    form = ReviewForm(request.POST)
    # checks if the user has submitted a review already
    existing_review = Review.objects.filter(userid=user, product=product)
    if existing_review.count() > 0:
        messages.error(request, 'Something went wrong! \
            You have reviewed this item already')
    else:
        if form.is_valid():
            review_form = form.save(commit=False)
            review_form.userid = user
            review_form.product = product
            review_form.save()
            messages.info(request, "Your review has been added now")
        else:
            messages.error(request, 'Failed to add review, \
                please ensure form is valid.')

    return redirect(reverse('product_detail', args=(product_id,)))


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.info(request, "Your review has been edited now")
        else:
            messages.error(request, 'Failed to edit review, \
                please ensure form is valid.')

    return redirect(reverse('product_detail', args=(review.product.id,)))


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.info(request, "Your review has been deleted now")

    return redirect(reverse('product_detail', args=(review.product.id,)))
