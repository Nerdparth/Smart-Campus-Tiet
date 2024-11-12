from django.contrib import admin
from .models import books_to_be_bought, Inventory, Books

admin.site.register(books_to_be_bought)
admin.site.register(Inventory)
admin.site.register(Books)
