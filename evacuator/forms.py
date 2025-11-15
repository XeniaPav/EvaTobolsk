from django.core.exceptions import ValidationError
from django.forms import ModelForm, CheckboxInput

from evacuator.models import Employees, Service, Contact, Static, Eva, Static,FAQ

class EmployeesForm(ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"

class CompanyForm(ModelForm):
    class Meta:
        model = Static
        fields = "__all__"

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class EvaForm(ModelForm):
    class Meta:
        model = Eva
        fields = "__all__"

class FAQForm(ModelForm):
    class Meta:
        model = FAQ
        fields = "__all__"