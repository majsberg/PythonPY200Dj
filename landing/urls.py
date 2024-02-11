from django.urls import path
from .views import TemplView #index_view

urlpatterns = [
    # TODO добавьте здесь маршрут для вашего обработчика отображения страницы приложения landing
    # path('', index_view, name='index'),
    path('', TemplView.as_view(), name='form'),
]