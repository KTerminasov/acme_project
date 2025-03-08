from django.shortcuts import render, get_object_or_404, redirect
from .forms import BirthdayForm
from .utils import calculate_birthday_countdown
from .models import Birthday
# Импортируем класс пагинатора
from django.core.paginator import Paginator
# Импортируем view-классы ListView, CreateView, UpdateView,
# DeleteView, DetailView
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
# Импортируем функцию для перенаправки после заполнения формы.
from django.urls import reverse_lazy


class BirthdayCreateView(CreateView):
    """View-класс для создания объектов модели Birthday."""

    model = Birthday
    form_class = BirthdayForm


class BirthdayUpdateView(UpdateView):
    """View-класс для изменения объектов модели Birthday."""

    model = Birthday
    form_class = BirthdayForm


class BirthdayListView(ListView):
    """View-класс для просмотра списка объектов моделей Birthday."""

    # Модель, с которой работает CBV.
    model = Birthday

    # Сортировка, применяемая при выводе списка объектов
    ordering = 'id'

    # Настройки пагинации
    paginate_by = 10


class BirthdayDeleteView(DeleteView):
    """View-класс для удаления объектов модели Birthday."""

    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    """View-класс для просмотра информации об объекте модели Birthday."""

    model = Birthday

    def get_context_data(self, **kwargs):
        # Получим словарь с контекстом.
        context = super().get_context_data(**kwargs)

        # Добавим в словарь новый ключ.
        context['birthday_countdown'] = calculate_birthday_countdown(
            # Дату рождения берем из объекта в словаре context.
            self.object.birthday
        )

        # Возвращаем словарь котекста.
        return context
