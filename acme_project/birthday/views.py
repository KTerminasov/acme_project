from django.shortcuts import render, get_object_or_404, redirect
from .forms import BirthdayForm
from .utils import calculate_birthday_countdown
from .models import Birthday
# Импортируем класс пагинатора
from django.core.paginator import Paginator
# Импортируем view-классы ListView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Импортируем функцию для перенаправки после заполнения формы.
from django.urls import reverse_lazy


class BirthdayMixin:
    """Класс, хранящий повторяющися код из view-классов модели Birthday."""

    # Модель, с которой работает класс. Он сам создаст форму на ее основе.
    model = Birthday

    # Используем только если форма создается от модели.
    # # Поля, которые должны быть в форме
    # fields = '__all__'

    # namespace:name для перенаправления после заполнения формы.
    success_url = reverse_lazy('birthday:list')


class BirthdayFormMixin:
    """Класс, хранящий повторяющися код для форм из view-классов модели Birthday."""

    # Указываем имя формы, которую нужно использовать
    form_class = BirthdayForm

    # Шаблон. Базовое имя: имя-модели_form.html
    template_name = 'birthday/birthday.html'


class BirthdayCreateView(BirthdayMixin, BirthdayFormMixin, CreateView):
    """View-класс для создания объектов модели Birthday."""


class BirthdayUpdateView(BirthdayMixin, BirthdayFormMixin, UpdateView):
    """View-класс для изменения объектов модели Birthday."""


class BirthdayListView(ListView):
    """View-класс для просмотра списка объектов моделей Birthday."""

    # Модель, с которой работает CBV.
    model = Birthday

    # Сортировка, применяемая при выводе списка объектов
    ordering = 'id'

    # Настройки пагинации
    paginate_by = 10


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    """View-класс для удаления объектов модели Birthday."""

    model = Birthday
    # Имя шаблона можно не указывать, тк оно соответствует рекомендуемому
    # в документации: имя-модели_confirm_delete.html
    # template_name = 'birthday/birthday_confirm_delete.html'
    success_url = reverse_lazy('birthday:list')
