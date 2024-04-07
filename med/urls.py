from django.urls import path

from med.views import HomeView, AboutView, DoctorView, PatientView, patient_create

app_name = "med"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("doctor/", DoctorView.as_view(), name="doctor"),
    path("bemor/", PatientView.as_view(), name="bemor"),
    path("patient/create/", patient_create, name="create-patient"),
]
