from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import ContactForm, LoginForm, RegisterForm, PasswordChange

def home_page(request):
    context = {
        "title":"HOME PAGE",
        "content":"WELCOME TO THE HOME PAGE."
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    form = ContactForm(request.POST or None)
    context = {
        "title":"CONATACT PAGE",
        "purpose":"CONTACT US",
        "bname":"Send Message",
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)

    return render(request, "contact/view.html", context)

def about_page(request):
    context = {
        "title":"ABOUT PAGE",
        "content":"WELCOME TO THE ABOUT PAGE."
    }
    return render(request, "about_page.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form,
        "title":"LOGIN PAGE",
        "purpose":"Log In",
        "bname":"Sign In",
    }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in successfully.')
            # Redirect to a success page.
            return redirect("/login")
        else:
            # Return an 'invalid login' error message.
            context['form'] = LoginForm()
            messages.add_message(request, messages.ERROR, 'Invalid User Name or Password')
    return render(request, "auth/login.html",context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form,
        "title":"REGISTER PAGE",
        "purpose":"Register Now",
        "bname":"Sign Up"

    }
    if form.is_valid():
            print(form.cleaned_data)
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            email=form.cleaned_data.get("email")
            first_name=form.cleaned_data.get("first_name")
            last_name=form.cleaned_data.get("last_name")
            new_user = User.objects.create_user(username, email,  password)
            new_user.last_name = last_name
            new_user.first_name = first_name
            new_user.save()
            login(request, new_user)
            messages.add_message(request, messages.SUCCESS, 'Registration Successfull')
            print(new_user)
            return redirect("/login")
    return render(request, "auth/register.html", context)

def logout_page(request):
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logged Out Successfully')
    return redirect("/login")

def password_change(request):
    form = PasswordChange(request.POST or None)
    context = {
        "form": form,
        "title":"PASSWORD CHANGE",
        "purpose":"Change Password",
        "bname":"Change Password",
    }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        new_password=form.cleaned_data.get("new_password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            u = User.objects.get(username=username)
            u.set_password(new_password)
            u.save()
            messages.add_message(request, messages.SUCCESS, 'Password Changed Successfully')
            return redirect("/login")
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            context['form'] = PasswordChange()
            messages.add_message(request, messages.ERROR, 'Invalid User Name or Password')
    return render(request, "auth/password_change.html",context)
