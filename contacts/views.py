from django.shortcuts import render, redirect
from contacts.forms import contactForm
from contacts.models import User_message,Contact_Info
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST or None)
        contact = User_message()
        if form.is_valid():
            contact.name = form.cleaned_data['name']
            contact.email = form.cleaned_data['email']
            contact.subject = form.cleaned_data['subject']
            contact.message = form.cleaned_data['message']
            contact.save()
            send_mail(
                    'New message from customers', 
                    f"Please visit your admin panel site to the message",
                    'ummasoft@gmail.com',['isayaelib@gmail.com'], fail_silently=False
                )
            messages.success(request, f'message sent')
            return redirect('contact')
        else:
            messages.error(request, f'please put in the valid infomation')
    contacts = Contact_Info.objects.all()
    form = contactForm()
    context = {
        'form':form,
        'contacts':contacts
    }
    return render(request, 'contact/contacts.html', context)
