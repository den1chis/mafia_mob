from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Game, Player

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('balance',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Game)
admin.site.register(Player)
