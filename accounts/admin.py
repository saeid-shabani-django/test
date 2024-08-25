from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username','first_name','email','age','phone_number']
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('age','phone_number')}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('age','phone_number')}),
    )


admin.site.register(CustomUser,CustomUserAdmin) #decorator

