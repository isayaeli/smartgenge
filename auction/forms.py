from django import forms

from auction.models import Auction

class bidForm(forms.Form):
    amount = forms.CharField()
    auction = forms.CharField()
    