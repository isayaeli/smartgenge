from django.shortcuts import render, redirect
from users.forms import loginForm, registerForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'please activate your smart genge account.'
            message = render_to_string('users/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email])
            email.send()
            return redirect('confirm')
        
    else:
        form = registerForm()
    context = {
        'form':form
    }
    return render(request, 'users/register.html',context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('login')
    else:
        return redirect('confirm-link')

def confirm_account(request):
    return render(request, 'users/confirm_acc.html',{})

def confirm_link(request):
    return render(request, 'users/confirm_link.html',{})




def login_request(request):
    if request.method == 'POST':
        form = loginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'logged in successful')
                return redirect('shop')
            else:
                messages.error(request, f'invalid username or password')
                return redirect('login')
        else:
            messages.error(request, f'invalid username or password')
            return redirect('login')
    form = loginForm()
    context ={
        'form':form
    }
    return render(request, 'users/login.html', context)

def logout_request(request):
    logout(request)
    return redirect('shop')



