from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordResetForm
from prompt_toolkit.validation import ValidationError
from django.utils.translation import gettext as _

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
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
        if email and not User.objects.filter(email=email).exists():
            self.add_error('email', _('Користувача з такою електронною поштою не знайдено.'))
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
