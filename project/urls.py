from django.contrib import admin
from django.urls import path
from main.views import admin_views, main_views, profile_views, authorization_views, registration_views, editing_profile_views, error404_views

urlpatterns = [
    path('', main_views.index_page, name="Главная"),
    path('profile', profile_views.profile_page, name="Профиль"),
    path('profile/<int:id>', profile_views.profile_page, name="Чей-то профиль"),
    path('registration', registration_views.registration_page, name = "Регистрация профиля"),
    path('authorization', authorization_views.authorization_page, name = "Авторизация профиля"),
    path('edit_profile', editing_profile_views.editing_profile_page, name = "Редактирование профиля"),
    path('error404', error404_views.error404_page, name = "Ошибка 404"),
    path('admin', admin_views.index_page, name="Админ. панель"),
]
