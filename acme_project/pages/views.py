# Импортируем класс TemplateView для наследования.
from django.views.generic import TemplateView
# Импортируем модель Birthday
from birthday.models import Birthday


class HomePage(TemplateView):
    # В атрибуте template_name обязательно указывается имя шаблона,
    # на основе которого будет создана возвращаемая страница.
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        # Получаем словарь контекста с помощью родительского метода.
        context = super().get_context_data(**kwargs)

        # Добавляем в словарь ключ total_counr;
        # значение ключа - число объектов модели Birthday.
        context['total_count'] = Birthday.objects.count()

        # Возвращаем измененный словарь контекста.
        return context

