from django.contrib import admin
from .models import Card

# Register your models here.


@admin.register(Card)
class CardModel(admin.ModelAdmin):
    list_filter = ('pos', 'timestamp')
    list_display = ('hebrew', 'hebrew_nikkud', 'english', 'pos', 'timestamp')
