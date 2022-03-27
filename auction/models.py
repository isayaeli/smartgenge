import math
from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.utils import timezone

# Create your models here.
class Auction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    minimum_bid = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='auction_images')
    published_on = models.DateTimeField(auto_now_add=True)
    ends_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    @property
    def status(self):
        if self.ends_on > timezone.now():
            return 'On Going'
        return 'Closed'
    
    
    @property
    def deadline(self):
        now = timezone.now()

        diff = self.ends_on - now
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds
            if seconds == 1:
                return str(seconds) + " second"
            else:
                return str(seconds) + " seconds"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute"
            else:
                return str(minutes) + " minutes"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour"
            else:
                return str(hours) + " hours"

        if diff.days >= 1 and diff.days < 30:
            days = diff.days
            if days == 1:
                return str(days) + " day"
            else:
                return str(days) + " days"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month"
            else:
                return str(months) + " months"

        if diff.days >= 365:
            years = math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year"
            else:
                return str(years) + " years"
    

    @property
    def ended_time(self):
        now = timezone.now()

        diff = now - self.ends_on
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds
            if seconds == 1:
                return str(seconds) + " second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        if diff.days >= 1 and diff.days < 30:
            days = diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years"



class Bider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    amount = models.DecimalField(max_length=255, max_digits=255, decimal_places=0)
    submited_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.user.username)


class BidDate(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    minimum_bid =  models.IntegerField(default=0)
    product = models.CharField(max_length=100, null=True)


    def __str__(self):
        return str(self.date.date())

    
   