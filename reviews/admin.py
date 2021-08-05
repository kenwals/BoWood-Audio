from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'review_title',
        'product',
    )

    ordering = ('review_title',)

admin.site.register(Review, ReviewAdmin)