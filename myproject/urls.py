from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),  # Маршрут для профиля
    path('logout/', views.logout_view, name='logout'),  # Маршрут для выхода из аккаунта
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
