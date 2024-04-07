from django.forms import ModelForm

from med.models import Patient


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
