from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def whatwedo(request):
    """ A view to return the what we do page """

    return render(request, 'home/whatwedo.html')

def contact(request):
    """ A view to return the contact page """

    return render(request, 'home/contact.html')

def gallery(request):
    """ A view to return the gallery page """

    return render(request, 'home/gallery.html')