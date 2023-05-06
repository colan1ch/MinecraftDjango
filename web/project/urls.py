from django.urls import path, include
from django.contrib import admin
from main.views import main_views, profile_views, authorization_views, servers, control_panel_views

urlpatterns = [
    path('', main_views.index_page, name="index"),
    path('profile/', profile_views.profile_page, name="profile"),
    path('profile/<int:id>/', profile_views.profile_page, name="profile"),
    path('edit_profile/', profile_views.editing_profile_page, name = "edit profile"),
    path('registration/', authorization_views.registration_page, name = "register"),
    path('login/', authorization_views.login_page, name = "login"),
    path('error404/', main_views.error404_page, name = "Ошибка 404"),
    path('admin/', admin.site.urls, name="Админ. панель"),
    path('servers/', servers.servers_page, name="servers"),
    path('create_server/', main_views.create_server_page, name="create server"),
    path('server/<int:server_id>/console', control_panel_views.console_page, name='console'),
    path('server/<int:server_id>/settings', control_panel_views.settings_page, name='settings'),
    path('server/<int:server_id>/world', control_panel_views.world_page, name='world'),
]