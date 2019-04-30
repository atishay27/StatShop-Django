from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(
            label='Full Name :',
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Your Full Name"
                    }
                )
            )
    email    = forms.EmailField(
            label='E-Mail :',
            widget=forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Your E-Mail"
                    }
                )
    )
    content  = forms.CharField(
            label='Message :',
            widget=forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder":"Your Message"
                    }
                )
    )

    def clean_email(self):
        email=self.cleaned_data.get("email")
        if not "gmail.com" in email :
            raise forms.ValidationError("Email Has to be Gmail")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(
            label='UserName',
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Enter Username"
                    }
                )
    )
    password = forms.CharField(
            label='Password',
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Enter Password"
                    }
                )
    )

class PasswordChange(forms.Form):
    username = forms.CharField(
            label='UserName',
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Enter Username"
                    }
                )
    )
    password = forms.CharField(
            label='Password',
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Enter Password"
                    }
                )
    )
    new_password = forms.CharField(
            label='New Password',
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Enter New Password"
                    }
                )
    )


class RegisterForm(forms.Form):
    first_name = forms.CharField(
            label='First Name :',
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Your First Name"
                    }
                )
            )
    last_name = forms.CharField(
            label='Last Name :',
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Your Last Name"
                    }
                )
            )
    email    = forms.EmailField(
            label='E-Mail :',
            widget=forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Your E-Mail"
                    }
                )
    )
    username = forms.CharField(
            label='UserName :',
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Enter Username"
                    }
                )
    )
    password = forms.CharField(
            label='Password :',
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Enter Password"
                    }
                )
    )
    password2 = forms.CharField(
            label='Confirm Password :',
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Confirm Password"
                    }
                )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is already used")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Password and Confirm Password Must Be Same")
        return data
