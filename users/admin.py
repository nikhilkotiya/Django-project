from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import SignUpForm, MyUserChangeForm
from .models import User, Profile



class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class MyUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    add_form = SignUpForm
    form = MyUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, MyUserAdmin)