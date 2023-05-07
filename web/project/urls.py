from django.urls import path, include
from django.contrib import admin
from main.views import main_views, profile_views, authorization_views, servers, control_panel_views, api

urlpatterns = [
    path('', main_views.index_page, name="home"),
    path('profile/', profile_views.profile_page, name="profile"),
    path('profile/<int:id>/', profile_views.profile_page, name="profile"),
    path('edit_profile/', profile_views.editing_profile_page, name = "edit profile"),
    path('registration/', authorization_views.RegisterUser.as_view(), name = "register"),
    path('login/', authorization_views.LoginUser.as_view(), name = "login"),
    path('error404/', main_views.error404_page, name = "Ошибка 404"),
    path('admin/', admin.site.urls, name="Админ. панель"),
    path('servers/', servers.servers_page, name="servers"),
    path('create_server/', servers.create_server_page, name="create server"),
    path('logout/', authorization_views.logout_user, name='logout'),

    path('server/<int:server_id>/console', control_panel_views.console_page, name='console'),
    path('server/<int:server_id>/settings', control_panel_views.settings_page, name='settings'),
    path('server/<int:server_id>/world', control_panel_views.world_page, name='world'),

    path('api/create_server', api.create_server),
    path('api/start_server/<int:server_id>', api.start_server),
    path('api/stop_server/<int:server_id>', api.stop_server),
    path('api/restart_server/<int:server_id>', api.restart_server),
    path('api/edit_server/<int:server_id>', api.edit_server),
    path('api/run_command/<int:server_id>', api.run_command),
    path('api/edit_version/<int:server_id>', api.edit_version_server),
]