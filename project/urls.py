from django.contrib import admin
from django.urls import path
from main.views import admin_views, main_views, profile_views, servers

urlpatterns = [
    path('', main_views.index_page, name="Главная"),
    path('profile', profile_views.profile_page, name="Профиль"),
    path('profile/<int:id>', profile_views.profile_page, name="Чей-то профиль"),
    path('servers', servers.servers_page, name="Сервера"),

    path('admin', admin_views.index_page, name="Админ. панель"),
]
