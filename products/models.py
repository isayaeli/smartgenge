from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save

class Product(models.Model):
    STATUS = (
        (0,'Draft'),
        (1,'Publish')
    ) 

    CATEGORIES = (
        ('fastfood','FastFood'),
        ('dried','Dried'),
        ('fruit','Fruit'),
        ('juice','Juice'),
        ('vegitable','Vegitable'),   
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True, choices=CATEGORIES)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
    # discount = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_length=255, max_digits=255, decimal_places=2, blank=True, null=True)
    discount_price = models.DecimalField(max_length=255, max_digits=255, decimal_places=2, blank=True, null=True)
    status = models.IntegerField(choices=STATUS)

    def __str__(self):
        return str(self.name)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('Wishlist_item' ,related_name='items', blank=True)
    updateon = models.DateTimeField(default=datetime.now())
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

def create_wishlist(sender, **kwargs):
    if kwargs['created']:
        wish = Wishlist.objects.create(user=kwargs['instance'])
post_save.connect(create_wishlist, sender=User)



class wishlist_item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listed_on = models.ForeignKey(Wishlist, on_delete=models.CASCADE, null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    updateon = models.DateTimeField(default=datetime.now())
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    

