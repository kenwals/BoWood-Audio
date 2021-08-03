from django.contrib import messages
from django.shortcuts import render
from .models import PhotoGallery
from django.core.mail import send_mail 

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def whatwedo(request):
    """ A view to return the what we do page """

    return render(request, 'home/whatwedo.html')

def contact(request):
    """ A view to return the contact page """
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message = request.POST['message']
        print(message_email)
        # send an email
        send_mail(
            message_subject + ': message from ' + message_name, # subject
            message + " RECEIVED FROM : " + message_email, # message
            message_email, # from email
            ['kenwals@gmail.com'], # To Email list
        )
        messages.info(request, f'Thank you {message_name}, Your message has been sent now!')

        return render(request, 'home/contact.html',{'message_name': message_name})

    else:
        return render(request, 'home/contact.html')

def gallery(request):
    """ A view to return the gallery page """

    photos = PhotoGallery.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, 'home/gallery.html', context)