from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),  # Маршрут для профиля
    path('logout/', views.logout_view, name='logout'),  # Маршрут для выхода из аккаунта
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('manage_balance/', views.manage_balance, name='manage_balance'),
    path('create_game/', views.create_game, name='create_game'),
    path('monitor_games/', views.monitor_games, name='monitor_games'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
    path('create_game/', views.create_game, name='create_game'),
]           