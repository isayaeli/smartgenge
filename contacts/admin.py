from django.contrib import admin
from contacts.models import User_message, Contact_Info

# Register your models here.
admin.site.register(User_message)
admin.site.register(Contact_Info)