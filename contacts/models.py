from django.db import models

# Create your models here.
class User_message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(default=True,null=True)

    def __str__(self):
        return self.name

class Contact_Info(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    website = models.URLField(max_length=255)

    def __str__(self):
        return f'Our contact info'



