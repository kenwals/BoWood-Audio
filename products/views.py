from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Product
from profiles.models import UserProfile
from reviews.models import Review
from reviews.forms import ReviewForm
from .forms import ProductForm


def all_products(request):
    """ A view to show all products, including sorting and searching """

    products = Product.objects.all()
    paginator = Paginator(products, 4) # Show 4 products per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter search criteria!")
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) | Q(description__icontains=query))
            # i ensures the query is case insensive!
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'page_obj': page_obj,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details  """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id)
    paginator = Paginator(reviews, 2) # shows 2 reviews per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = ReviewForm()
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
    else:
        user = None

    # If user has reviewed an item
    try:
        # retrieve review for selected item by user
        item_review = Review.objects.get(userid=user, product=product)

        # get a prefilled form with specific review
        edit_review_form = ReviewForm(instance=item_review)

    # If there are no reviews by the user
    except Review.DoesNotExist:
        edit_review_form = None

    context = {
        'product': product,
        'reviews': reviews,
        'page_obj': page_obj,
        'review_form': form,
        'edit_review_form': edit_review_form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
