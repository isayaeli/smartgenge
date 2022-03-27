from django.contrib import admin
from .models import Auction, Bider, BidDate
from django.contrib.auth.models import Group
# Register your models here.
admin.site.register(Auction)
admin.site.register(BidDate)

class BiderAdmin(admin.ModelAdmin):
    search_fields = ["amount",]


admin.site.register(Bider, BiderAdmin)

admin.site.site_header = 'KaziConnect Admin'
admin.site.unregister(Group)