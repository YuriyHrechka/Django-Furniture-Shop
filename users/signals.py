from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from carts.models import Cart


@receiver(user_logged_in)
def assign_cart_to_user(sender, request, user, **kwargs):
    session_key = request.session.session_key

    if session_key:
        Cart.objects.filter(
            session_key=session_key, user__isnull=True).update(user=user)
