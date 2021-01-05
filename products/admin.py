from django.contrib import admin
from products.models import Product, Wishlist, wishlist_item

admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(wishlist_item)

