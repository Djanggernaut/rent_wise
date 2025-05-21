from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserForm
from .utils import send_verification_email

from django.utils.http import urlsafe_base64_decode
from .models import User
from django.contrib.auth.tokens import default_token_generator

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect("index")
    elif request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            return redirect("login")
    return render(request, "accounts/login.html")

def logout(request):
    auth.logout(request)
    return redirect("login")

def register_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    elif request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            # Create the user using form
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.save()

            # Send verification email
            mail_subject = 'Please activate your account'
            email_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, email_template)

            return redirect('register_user')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()

    context = {
        'form':form,
    }

    return render(request, 'accounts/register_user.html', context)

def activate(request, uidb64, token):
    # Activate the user by setting the is_active status to True
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('index')
    else:
        return redirect('index')