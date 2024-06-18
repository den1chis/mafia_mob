from django.contrib import admin
from .models import Game, Player



admin.site.register(Game)
admin.site.register(Player)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('balance',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
