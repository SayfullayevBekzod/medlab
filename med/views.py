from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from med.forms import PatientCreateForm
from med.models import Count, Doctor, Patient


class HomeView(TemplateView):
    template_name = "index.html"


class AboutView(ListView):
    model = Count
    template_name = "med/about.html"
    context_object_name = "count"


class DoctorView(ListView):
    model = Doctor
    template_name = "med/doctor.html"
    context_object_name = "doctor"


class PatientView(ListView):
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
