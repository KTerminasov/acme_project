from django.contrib import admin
from django.urls import include, path, reverse_lazy
# Импортируем настройки проекта
from django.conf import settings
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static
# Импортируем классы для регистрации пользователей.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
    # Добавляем CBV для регистрации без создания views.py (наследуется)
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
    # Подключаем urls.py встроенного приложения для работы с пользователями.
    path('auth/', include('django.contrib.auth.urls')),    
    # В конце добавляем к списку вызов функции static.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Переопределяем хендлер андреса view-функции с ошибкой 404.
handler404 = 'core.views.page_not_found'
