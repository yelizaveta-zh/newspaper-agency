from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Topic, Redactor, Newspaper


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = ("id", "username", "email", "years_of_experience", "is_staff")
    search_fields = ("username", "email")
    list_filter = ("years_of_experience", "is_staff")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("years_of_experience",)}),
    )


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "published_date", "topic")
    search_fields = ("title", "content")
    list_filter = ("published_date", "topic")

    def has_add_permission(self, request):
        return request.user.is_staff and request.user.is_authenticated

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff and request.user.is_authenticated

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff and request.user.is_authenticated
