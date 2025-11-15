from operator import index

from django.urls import path

from evacuator.apps import EvacuatorConfig
from evacuator.views import HomeView, EmployeesListView, ServiceListView, EvaListView,CompanyView, ContactCreateView

app_name = EvacuatorConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("employees/", EmployeesListView.as_view(), name="employees_list"),
    path("service/", ServiceListView.as_view(), name="service_list"),
    path("eva/", EvaListView.as_view(), name="eva_list"),
    path("company/", CompanyView.as_view(), name="company"),
    path("contacts/", ContactCreateView.as_view(), name="contact_form"),

]
