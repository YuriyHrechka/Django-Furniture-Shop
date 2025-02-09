from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from carts.models import Cart
from orders.models import OrderItem, Order
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    # success_url = reverse_lazy('main:index')

    def get_success_url(self):
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('users:logout'):
            return redirect_page
        return reverse_lazy('main:index')

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.get_user()

        if user:
            auth.login(self.request, user)
            messages.success(self.request, f'{user.username}, Ви ввійшли в акаунт')
            if session_key:
                # delete old authorized user carts
                forgot_carts = Cart.objects.filter(user=user)
                if forgot_carts.exists():
                    forgot_carts.delete()
                # add new authorized user carts from anonymous session
                Cart.objects.filter(session_key=session_key).update(user=user)

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Авторизація'
        return context


class UserRegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        user = form.save(commit=False)

        try:
            user.save()
            session_key = self.request.session.session_key

            auth.login(self.request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            messages.success(self.request, f'{user.username}, Ви успішно зареєструвались та ввійшли в акаунт')
            return HttpResponseRedirect(self.success_url)

        except Exception as e:
            messages.error(self.request, 'Помилка під час реєстрації. Будь ласка, спробуйте ще раз.')
            return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Регістрація'
        return context


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Профіль успішно оновлено')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Сталася помилка')
        return super().form_invalid()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Кабінет'
        context['orders'] = Order.objects.filter(user=self.request.user).prefetch_related(
            Prefetch(
                'orderitem_set',
                queryset=OrderItem.objects.select_related('product'),
            )
        ).order_by('-id')

        return context


class UserCartView(TemplateView):
    template_name = 'users/users_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Кошик'
        return context


@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, Ви вийшли з акаунта')
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#
#             session_key = request.session.session_key
#
#             if user:
#                 auth.login(request, user)
#                 messages.success(request, f'{user.username}, Ви ввійшли в акаунт')
#
#                 if session_key:
#                     # delete old authorized user carts
#                     forgot_carts = Cart.objects.filter(user=user)
#                     if forgot_carts.exists():
#                         forgot_carts.delete()
#                     # add new authorized user carts from anonymous session
#                     Cart.objects.filter(session_key=session_key).update(user=user)
#
#                 redirect_page = request.POST.get('next', None)
#                 if redirect_page and redirect_page != reverse('users:logout'):
#                     return HttpResponseRedirect(request.POST.get('next'))
#
#                 return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserLoginForm()
#
#     context = {
#         'title': 'Home - Авторизація',
#         'form': form,
#     }
#     return render(request, 'users/login.html', context)

# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#
#             session_key = request.session.session_key
#
#             user = form.instance
#             auth.login(request, user)
#
#             if session_key:
#                 Cart.objects.filter(session_key=session_key).update(user=user)
#
#             messages.success(request, f'{user.username}, Ви успішно заєреструвались та ввійшли в акаунт')
#             return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserRegistrationForm()
#
#     context = {
#         'title': 'Home - Регістрація',
#         'form': form,
#     }
#     return render(request, 'users/registration.html', context)

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Профіль успішно оновлено')
#             return HttpResponseRedirect(reverse('user:profile'))
#     else:
#         form = ProfileForm(instance=request.user)
#
#     orders = (
#         Order.objects.filter(user=request.user).prefetch_related(
#             Prefetch(
#                 'orderitem_set',
#                 queryset=OrderItem.objects.select_related('product'),
#             )
#         ).order_by('-id')
#     )
#     context = {
#         'title': 'Home - Кабінет',
#         'form': form,
#         'orders': orders,
#     }
#     return render(request, 'users/profile.html', context)

# def users_cart(request):
#     return render(request, 'users/users_cart.html') 
