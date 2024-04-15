from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, TemplateView

from med.forms import PatientCreateForm, PatientForm, UserLoginForm
from med.models import Count, Doctor, Patient, PatientDoctor, Department


class HomeView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "med/about.html"


class DoctorView(ListView):
    model = Doctor
    template_name = "med/doctor.html"
    context_object_name = "doctor"


class PatientView(ListView):
    paginate_by = 20
    model = Patient
    template_name = "med/patient.html"
    context_object_name = "bemor"


@login_required()
def patient_create(request):
    if request.method == "POST":
        form = PatientCreateForm(request.POST)
        if form.is_valid():
            patient = Patient(
                fullname=form.cleaned_data["fullname"],
                age=form.cleaned_data["age"],
                gender=form.cleaned_data["gender"],
                disease_id=form.cleaned_data["disease_id"],
            )
            patient.save()
            messages.success(request, "Bemor mufafiqiyatli qo'shildi")
            return redirect(reverse("med:bemor"))
        else:
            return render(request, "med/patient_form.html", {"form": form})
    else:
        form = PatientCreateForm()
        return render(request, "med/patient_form.html", {"form": form})


def doctor_view(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PatientForm()
    return render(request, "med/appoint.html", {"form": form})


class Acceptance(ListView):
    model = PatientDoctor
    template_name = "med/acceptance.html"
    context_object_name = "acceptance"


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "User successfully loged out")
        return redirect("med:home")


class LoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "user/login.html", {"form": form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"you have login as {username}")
                return redirect("med:home")
            else:
                messages.error(request, "Wrong username or password")
                return render(request, "user/login.html", {"form": form})
        else:
            return render(request, "user/login.html", {"form": form})


class ServicesView(TemplateView):
    template_name = "med/services.html"


class DepartmentView(ListView):
    model = Department
    template_name = "med/departments.html"
    context_object_name = "departments"


class Contact(TemplateView):
    template_name = "med/contact.html"
