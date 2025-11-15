from django.contrib import admin

from evacuator.models import Employees, Service, Contact, Static, FAQ


@admin.register(Employees)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "specialization", "avatar", "comment")
    list_filter = ("specialization",)
    search_fields = ("name",)


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("id", "service_name", "price")
    list_filter = ("price",)
    search_fields = ("service_name",)


@admin.register(Static)
class StaticAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "submitted_at",
        "name",
        "phone",
        "photo",
        "message"
    )

@admin.register(FAQ)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "answer",)

