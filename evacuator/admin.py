from django.contrib import admin

from evacuator.models import Employees, Service, Contact, Static, FAQ, Eva


@admin.register(Eva)
class EvaAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "Weight", "avatar", "comment")
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "specialization", "avatar", "comment")
    list_filter = ("specialization",)
    search_fields = ("name",)


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("id", "service_name", "price")
    list_filter = ("price",)


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
class FAQAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "answer",)

