from django.contrib import admin
from cart.models import *

class CartAdmin(admin.ModelAdmin):
	list_display = ['user', 'odered']

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
admin.site.register(Order)
