from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


# # Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_active")
    list_filter = ("is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login",)}),
    )

    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
