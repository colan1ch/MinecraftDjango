from django.urls import path, include
from django.contrib import admin
from main.views import admin_views, main_views, profile_views, authorization_views, servers

urlpatterns = [
    path('', main_views.index_page, name="Главная"),
    path('profile/', profile_views.profile_page, name="Профиль"),
    path('profile/<int:id>/', profile_views.profile_page, name="Чей-то профиль"),
    path('edit_profile/', profile_views.editing_profile_page, name = "Редактирование профиля"),
    path('registration/', authorization_views.registration_page, name = "Регистрация"),
    path('login/', authorization_views.login_page, name = "Логин"),
    path('error404/', main_views.error404_page, name = "Ошибка 404"),
    path('admin/', admin.site.urls, name="Админ. панель"),
    path('servers/', servers.servers_page, name="Сервера"),
]