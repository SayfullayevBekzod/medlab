from django.forms import ModelForm
from django import forms
from med.models import Patient, PatientDoctor


class PatientCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if str(field) != "is_active":
                self.fields[field].widget.attrs.update(
                    {"class": "form-control", "placeholder": f"Enter the {str(field)}"}
                )

    class Meta:
        model = Patient
        fields = ("fullname", "age", "gender", "disease_id")


class PatientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if str(field) != "is_active":
                self.fields[field].widget.attrs.update(
                    {"class": "form-control", "placeholder": f"Enter the {str(field)}"})

    class Meta:
        model = PatientDoctor
        fields = ("name", "age", "sickness", 'doctor', 'appointment_date')
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'})
        }
