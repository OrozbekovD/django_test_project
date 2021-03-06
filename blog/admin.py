from django.utils.translation import gettext, gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import Post, Author, Category, CustomUser, Comments, Ad


@admin.register(CustomUser)
class CustomUser(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_premium', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username','first_name', 'last_name', 'is_staff', 'is_premium')

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Ad)
