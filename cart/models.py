
from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from datetime import datetime
from django_countries.fields import CountryField
from django.db.models.signals import post_save


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True)
    ordered = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
    def get_total_price(self):
        return self.product.price * self.quantity

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem, related_name='items' ,blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    odered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_line_total(self):
        total = 0
        for cart_item in self.items.all():
            total = total + cart_item.get_total_price()
        return total


def create_cart(sender, **kwargs):
    if kwargs['created']:
        cart = Cart.objects.create(user=kwargs['instance'])
post_save.connect(create_cart, sender=User)



class Order(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    address = models.CharField(max_length=100)
    second_address =models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    placed_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username



