# from django import forms
# from cart.models import Order
# from django_countries.fields import CountryField
# from django_countries.widgets import CountrySelectWidget

# PAYMENT = (
# 	('S','Stripe'),
# 	('P','Paypal'),
#     ('C','Cash On Delivery')
# )
# class checkoutForm(forms.Form):
#     country = CountryField(blank_label='selecy your country').formfield(widget=CountrySelectWidget(attrs={'class':'form-control'}))
#     address = forms.CharField(widget=forms.TextInput(
#         attrs={'class':'form-control', 'placeholder':'Appartment, suite'}), label=" first Address")

#     second_address = forms.CharField(widget=forms.TextInput(
#         attrs={'class':'form-control','placeholder':'Optional'}), required=False, label="Second Address")

#     city = forms.ChoiceField(widget=forms.TextInput(
#         attrs={'class':'form-control', 'placeholder':'eg. Dar es salaam'}), label="City/Town")

#     zip_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Zip Code")

#     phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Phone")
#     # email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), label="Email")
#     payment = forms.ChoiceField(widget=forms.RadioSelect(), choices=PAYMENT)

#     class Meta:

#         model = Order

from django import forms
from cart.models import Cart,Order
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget



PAYMENT = (
    ('S','Stripe'),
    ('C','cash on Delivery')
)

class checkoutForm(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Adress")
    second_address = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}), required=False, label="Second Address")
    country = CountryField(blank_label='selecy your country').formfield(
        widget=CountrySelectWidget(attrs={'class':'form-control'}))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Phone")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), label="Email")
    payment = forms.ChoiceField(widget=forms.RadioSelect(), choices=PAYMENT)


    class Meta:
        modal = Order
        fields = [
            'address','second_address','country'
        ]

