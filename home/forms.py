from django import forms
from django.forms import fields
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        subject_choices= [
            ('General', 'General Query'),
            ('Booking', 'Booking Query'),
            ('Editing', 'Editing Query'),
        ]


        widgets = {
            'name': forms.TextInput(attrs={ 'placeholder':'Please enter your full name' }),
            'email': forms.EmailInput(attrs={ 'placeholder':'email@example.com' }),
            'subject': forms.Select(choices=subject_choices)
        }

