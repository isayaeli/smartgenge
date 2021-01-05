from django import forms
from contacts.models import User_message


class contactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Your Name'}), label='Name')
        
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Your Email'}), label='Email') 

    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'subject'}), label='Subject')

    message = forms.CharField(widget=forms.Textarea(
        attrs={'class':'form-control','placeholder':'Message','cols':30, 'rows':7}), label='Message') 

    
    class Meta:
        model = User_message
        fields = '__all__'