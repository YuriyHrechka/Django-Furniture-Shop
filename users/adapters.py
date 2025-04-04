from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
import random
import string
from django.core.exceptions import ValidationError
from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import redirect

from django.contrib.auth import get_user_model

User = get_user_model()


def generate_random_string(length=4):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)

        self.set_first_name(user, data)
        self.set_last_name(user, data)
        self.set_email(user, data)
        self.set_username(user, data)

        return user

    def set_first_name(self, user, data):
        if not user.first_name:
            user.first_name = data.get('first_name', '')

    def set_last_name(self, user, data):
        if not user.last_name:
            user.last_name = data.get('last_name', '')

    def set_email(self, user, data):
        if not user.email:
            user.email = data.get('email', '')

    def set_username(self, user, data):
        if not user.username and data.get('email'):
            base_username = data.get('email').split('@')[0]
            username = f"{base_username}_{generate_random_string()}"

            if self.is_username_taken(username):
                username = self.generate_unique_username(base_username)

            user.username = username

    def is_username_taken(self, username):
        return User.objects.filter(username=username).exists()

    def generate_unique_username(self, base_username):
        while True:
            username = f"{base_username}_{generate_random_string()}"
            if not self.is_username_taken(username):
                return username

# class CustomAccountAdapter(DefaultAccountAdapter):
#     def is_open_for_signup(self, request):
#         return False
