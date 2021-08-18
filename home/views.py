from django.contrib import messages
from django.shortcuts import render
from .models import PhotoGallery
from .forms import ContactForm
from django.core.mail import send_mail


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def whatwedo(request):
    """ A view to return the what we do page """

    return render(request, 'home/whatwedo.html')


def contact(request):
    """
    This view populates and takes messages
    from the contact page
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            message_name = request.POST['name']
            message_email = request.POST['email']
            message_subject = request.POST['subject']
            message = request.POST['message']
            print(message_email)
            # send an email
            send_mail(
                message_subject + ': message from ' + message_name,
                message + " RECEIVED FROM : " + message_email,
                message_email,
                ['kenwals@gmail.com'],
            )
            return render(request, 'home/contact.html', {
                'message_name': message_name})
        else:
            messages.error(request, 'Failed to send message, \
                please ensure fields are filled in correctly.')

    else:
        form = ContactForm()
        return render(request, 'home/contact.html', {'form': form})


def gallery(request):
    """ This views passed photo to the gallery page """

    photos = PhotoGallery.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, 'home/gallery.html', context)
