from django import forms
from blog.models import BlogComment

class commentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':3,}),required=True)

    class Meta:
        model = BlogComment
        fields = ['content']