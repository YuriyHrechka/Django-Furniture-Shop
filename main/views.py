from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Головна'
        context['content'] = 'Магазин меблів HOME'
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Про нас'
        context['content'] = 'Про нас'
        context['text_on_page'] = 'Текст про те чому цей магазин такий класний, і який гарний товар'
        return context

# def index(request):
#     context = {
#         'title': 'Home - Головна',
#         'content': 'Магазин меблів HOME',
#     }
#     return render(request, 'main/index.html', context)


# def about(request):
#     context = {
#         'title': 'Home - Про нас',
#         'content': 'Про нас',
#         'text_on_page': 'Текст про те чому цей магазин такий класний, і який гарний товар'
#     }
#     return render(request, 'main/about.html', context)
