from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from evacuator.forms import (
    EmployeesForm,
    ServiceForm,
    ContactForm,
    CompanyForm,
    EvaForm
)

from evacuator.models import Employees, Service, Contact, Static, Eva, FAQ

# Create your views here.
class HomeView(TemplateView):
    """Главная страница сайта"""

    template_name = "evacuator/index.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        companies = Static.objects.all()
        question = FAQ.objects.all()
        context_data["all_companies"] = companies.order_by()
        context_data["all_question"] = question.order_by()
        return context_data

class EmployeesListView(ListView):
    """Отображение списка сотрудников"""

    model = Employees


class EvaListView(ListView):
    """Отображение списка техники"""

    model = Eva

class ServiceListView(ListView):
    """Отображение списка услуг"""

    model = Service


class CompanyView(TemplateView):
    """Страница "О компании" """

    template_name = "evacuator/company.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        companies = Static.objects.all()
        context_data["all_companies"] = companies.order_by()
        return context_data



class ContactCreateView(CreateView):
    """Создание сообщения"""

    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("evacuator:contact_form")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        companies = Static.objects.all()
        context_data["all_companies"] = companies.order_by()
        return context_data
