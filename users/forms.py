from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput()
    )
    password = forms.CharField(
        widget=forms.PasswordInput
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

