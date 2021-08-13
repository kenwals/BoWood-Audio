from products.models import Product
from django import forms
from django.forms import fields
from .models import Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('rating', 'review_title', 'review_text')
        labels = {
            'rating': 'Rating', 
            'review_title': 'Title', 
            'review_text': 'Review'
        }

        rating_choices = [
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        ]

        widgets = {
            'review_title': forms.TextInput(attrs={ 'placeholder':'Enter your review title here' }),
            'review_text': forms.Textarea(attrs={ 'placeholder':'Enter your review here' }),
            'rating': forms.Select(choices=rating_choices)
        }

