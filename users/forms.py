from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordResetForm
from django.contrib.auth import get_user_model
from prompt_toolkit.validation import ValidationError
from django.utils.translation import gettext as _

from allauth.socialaccount.forms import SignupForm
from django import forms

from users.models import User

UserModel = get_user_model()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput()
    )
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    # username = forms.CharField(
    #     label='Ім\'я користувача',
    #     widget=forms.TextInput(attrs={'autofocus': True,
    #                                   'class': 'form-control',
    #                                   'placeholder': 'Введіть ваше ім\'я користувача'})
    # )
    # password = forms.CharField(
    #     label='Пароль',
    #     widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
    #                                       'class': 'form-control',
    #                                       'placeholder': 'Введіть ваш пароль'})
    # )


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class CustomPasswordResetForm(PasswordResetForm):
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if email:
            user_qs = User._default_manager.filter(email__iexact=email, is_active=True)
            if not user_qs.exists():
                self.add_error('email', _('Користувача з такою електронною поштою не знайдено.'))
            else:
                if not user_qs.filter(session_auth=True).exists():
                    self.add_error('email',
                                   _('Скидання пароля неможливе: ваш акаунт не підходить для цієї операції.'))
        return cleaned_data


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
        )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()

# class MySocialSignupForm(SignupForm):
#     username = forms.CharField(max_length=30, label='Імʼя користувача', required=True)
#
#     def save(self, request):
#         user = super(MySocialSignupForm, self).save(request)
#         user.username = self.cleaned_data['username']
#         user.save()
#         return user
