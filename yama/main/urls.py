from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('accounts/registration', views.registration, name='registration'),
    path('debt_create', views.debt_create, name='debt_create'),
    path('debt_delete/<int:debt_id>', views.debt_delete, name='debt_delete'),
]
