from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('Klienci/',views.KlientLista.as_view()),
    path('Przystanki/',views.PrzystanekLista.as_view()),
    path('Trasy/',views.TrasaLista.as_view()),
    path('Kursy/',views.KursLista.as_view()),
    path('Bilety/',views.BiletyLista.as_view()),
]